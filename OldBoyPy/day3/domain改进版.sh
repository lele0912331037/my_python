#!/bin/bash
sed -i 's/\r//' hosts
#获取所有域名
sed 's/\r//g' hosts | grep -v "^$" | grep -v '#' | grep -v localhost | awk '{print $2}' | awk -F. '{if(($(NF-1)!~"google")&&($(NF-2)~"google")&&(NF>="3")) print $(NF-2)"."$(NF-1)"."$NF ; else if(NF>="2") print$(NF-1)"."$NF ; else print $NF}' | sort -u > realhost
#获取所有域名的总数
num1=`sed 's/\r//g' hosts | grep -v "^$" | grep -v '#' | grep -v localhost | awk '{print $2}' | awk -F. '{if(($(NF-1)!~"google")&&($(NF-2)~"google")&&(NF>="3")) print $(NF-2)"."$(NF-1)"."$NF ; else if(NF>="2") print$(NF-1)"."$NF ; else print $NF}' | sort -u | wc -l `
zfile='/etc/named.rfc1912.zones'
dnsdir='/var/named'
bzfile='/etc/named.rfc1912.zones.bak'
log1=`var/log/named.log1`
new_name_su=0
new_zone_su=0
new_host_su=0
adddp_host_su=0
addcover_host_su=0
add_host_su=0
if [[ -f $log1 ]]; then
  echo "`date` " >> $log1
else
  touch $log1
  echo "`date` " >> $log1
fi
if [ -f $bzfile ];
then
        mv $bzfile /tmp/`date +%Y%m%d%H%m%s`-named.rfc1912.zones.bak
        cp $zfile $bzfile
else
        cp $zfile $bzfile
fi
for((i=1;i<=$num1;i++))
do
		domain=`awk -F. 'NR=='$i' {print $0}' realhost` #取出域名
		if [[ `cat $zfile | grep \"$domain\" | wc -l ` -lt 1 ]];then #判断是否存在域名解析记录
      zone="zone \"$domain\" IN {\n\ttype master;\n\tfile \"$domain.zone\";\n\tallow-update { none; };\n};\n"
      echo -e $zone >> $zfile
      if [[ $? -eq 0 ]]; then #判断追加域名结果，并计算成功和失败个数
        let "new_name_su += 1"
      fi
		fi
    num2=`grep \.$domain$ hosts | grep -v "#" | grep -v "^$" | grep -v localhost | wc -l` #计算包括此域名在hosts文件的个数
    if [[ `ls $dnsdir | grep ^$domain.zone | wc -l ` -lt 1 ]];then #判断/var/named/是否有此域名的zone文件，没有则执行
      name="\$TTL 86400\n@\tIN\tSOA\tdns.$domain. root. (\n\t\t\t\t\t42\t; serial\n\t\t\t\t\t3H\t; refresh\n\t\t\t\t\t15M\t; retry\n\t\t\t\t\t1W\t; expire\n\t\t\t\t\t1D )\t; minimum\n\tIN\tNS\tdns."
      echo -e $name > $dnsdir/$domain.zone 
      if [[ $? -eq 0 ]]; then 
        let "new_zone_su +=1"
      fi  
      for (( j = 1; j <= num2; j++ )); do #循环此域名的个数
        ip=`grep \.$domain$ hosts | grep -v '#' | grep -v "^$"| grep -v localhost | awk 'NR=='$j'{print $1}'` #截取此条域名对应的IP
        host=`grep \.$domain$ hosts |grep -v '#' | grep -v "^$" | awk 'NR=='$j'{print $2}' | awk -F".$domain" '{print $1}' | grep -v $domain` #截取此条域名的主机名
        echo -e "$host\tIN\tA\t$ip" >> $dnsdir/$domain.zone #追加此域名的所有A记录
        echo "1"
        if [[ $? -eq 0 ]]; then 
          let "new_host_su +=1"
        fi  
      done
      echo "新建$domain：$new_host_su 个A记录。成功" >> $log1
      #echo "新建$domain：$new_host_fa 个A记录。失败" >> /var/log/named.log1
    else #判断/var/named/是否有此域名的zone文件，有则执行
      for (( z = 1; z <= num2; z++ )); do #循环此域名的个数
        #截取hosts文件中此条域名对应的IP
        ip=`grep \.$domain$ hosts | grep -v '#' | grep -v "^$"| grep -v localhost | awk 'NR=='$z'{print $1}'`
        #截取hosts文件中此条域名的主机名
        host=`grep \.$domain$ hosts |grep -v '#' | grep -v "^$" | awk 'NR=='$z'{print $2}' | awk -F".$domain" '{print $1}' | grep -v $domain`
        #获取此域名zone文件有对应主机名的个数
        zone_num=`grep "$host" $dnsdir/$domain.zone | grep -v ^$'\t\t' | grep -v '^\@' | grep -v '^\$' | grep -v '\dns.$' | grep -v '^\$'| wc -l `
        #判断是否有此域名对应A记录的主机名，有则执行以下循环
        if [[ $zone_num > 0 ]]; then
          for (( x = 1; x <= $zone_num ; x++ )); do #循环有相同主机名的条目
            zone_ip=`grep "$host" $dnsdir/$domain.zone  | grep -v ^$'\t\t' | grep -v '^\@' | grep -v '^\$' | grep -v '\dns.$' | grep -v '^\$' |awk -F"\t" 'NR=='$x' {print $NF}'` #获取此域名中与$hosts相同的的IP
            #判断此A记录的连通性，只用了ping检测，如果通，就追加一条相同主机名的A记录，不通则覆盖此条A记录。
            if [[ `ping -c 2 $zone_ip | grep ttl | wc -l ` > 0 ]]; then
              echo -e "$host\tIN\tA\t$ip" >> $dnsdir/$domain.zone 
              if [[ $? -eq 0 ]]; then #判断增加主机名重复的A记录结果，并计算成功和失败个数
                let "adddp_host_su +=1"
              fi
            else
              sed -i 's/$zone_ip/$ip/g' $dnsdir/$domain.zone
              if [[ $? -eq 0 ]]; then
                let "addcover_host_su +=1"
              fi
            fi
          done
        # 没有直接添加
        else
          echo -e "$host\tIN\tA\t$ip" >> $dnsdir/$domain.zone 
          if [[ $? -eq 0 ]]; then
            let "add_host_su +=1"
          fi
        fi
      done
      echo "$domain.zone成功追加重复：$adddp_host_su 个A记录" >> $log1
      echo "$domain.zone文件成功覆盖：$addcover_host_su 个A记录" >> $log1
      echo "$domain.zone成功追加：$add_host_su 个A记录" >> $log1
    fi
done
echo "新建域名：$new_name_su 个A记录" >> $log1
/etc/init.d/named restart >> /dev/null
if [[ $? -eq 0 ]]; then
  echo "`date`: named重启:成功" >> $log1
else
  echo "`date`: named重启:失败，请查看日志" >> $log1
fi

