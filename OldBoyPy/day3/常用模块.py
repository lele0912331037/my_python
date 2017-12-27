#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# random 生成随机数
import random

print(random.random())  # <0 >1 的浮点数
print(random.randint(1, 5))  # >=1 <=5 的整数
print(random.randrange(1, 5))  # >=1 <5 的整数

# 生成随机字母，通过chr转换
print(chr(random.randint(65, 90)))

# 生成类似的验证码，数字加字母组合
a = ''
for i in range(6):
    if i == random.randint(0, 5) or i == random.randint(0, 5):
        a += chr(random.randint(48, 57))
    else:
        a += chr(random.randint(65, 90))
print(a)

# join,格式化list
li = ['1\r\n11', '2', '3', '4', '5']
print('join,格式化list:', '\n'.join(li))

# md5加密 引用 hashlib模块
import hashlib

md5 = hashlib.md5()
md5.update('admin'.encode('utf-8'))
md5.update('@123'.encode('utf-8'))
print('md5加密:', md5.hexdigest())

# sha1加密 引用 hashlib模块
sha1 = hashlib.sha1()
sha1.update('admin'.encode('utf-8'))
sha1.update('admin'.encode('utf-8'))
print('sha1加密：', sha1.hexdigest())


def get_md5(password):
    # 弱密码加盐
    md5_1 = hashlib.md5()
    md5_1.update((password+'@123').encode('utf-8'))
    return md5_1.hexdigest()
print(get_md5('admin'))

# 序列化和json
# 序列化：python 内部转换格式
import pickle
li = ['alex', 11, 22, 'ok', 'sb']

# 转换成字符串或二进制形式
dump_temp = pickle.dumps(li)
print(dump_temp, type(dump_temp))
load_sed = pickle.loads(dump_temp)
print(load_sed, type(load_sed))

# 转换成字符串或二进制形成，并写入文件
pickle.dump(li, open('test.txt', 'wb'))
print(pickle.load(open('test.txt', 'rb')))

# json
import json
name_dic = {'name': 'yinxl', 'age': '23'}
print(json.dumps(name_dic), type(json.dumps(name_dic)))
print(json.loads(json.dumps(name_dic)), type(json.dumps(name_dic)))

json.dump(name_dic, open('test1.txt', 'w'))
print(json.load(open('test1.txt', 'r')))

# re
import re
li = 'dfuui192.168.30.23dshjbe10.10.1.2rvbnk010-234444skrfebjasjw2016-03-04'

# match 从头开始找
result = re.match('\d+', li)
print(result.group()) if result else print('nothing')

# search 整个字符串
result2 = re.search('\d+', li)
print(result2.group() if result2 else print('nothing'))

# findall 匹配所有满足条件
result3 = re.findall('\d+', li)
print(result3)

# compile
com = re.compile('(?:2[0-4]\d\.|25[0-5]\.|[01]?\d\d?\.){3}(?:2[0-4]\d|25[0-5]|[01]?\d\d?)')
com1 = re.compile(r'(?:(?:[0-1]?\d{0,2}|2[0-4]\d|25[0-5])\.){3}(?:[0-1]?\d{0,2}|2[0-4]\d|25[0-5])')
print(com.search(li).group(), '\n', com1.search(li).group())
print(com.findall(li), "\n", com1.findall(li))

# 正则表达式,匹配ip地址
# (?: pattern)是非捕获型括号，匹配pattern，不捕获匹配结果
# (?:(?:[0-1]?\d{0,2}|2[0-4]\d|25[0-5])\.){3}(?:[0-1]?\d{0,2}|2[0-4]\d|25[0-5])
# (?:(?:2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(?:2[0-4]\d|25[0-5]|[01]?\d\d?)

# time
import time
# 时间戳的形式
print(time.time())
print(time.mktime(time.localtime()))
# 元祖形式
print(time.localtime())
print(time.gmtime())
# 字符串形式
print('字符串形式\n', time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.ctime())

## sys模块
#import sys
#sys.argv        # 命令行参数List，第一个元素是程序本身路径
## sys.exit(n)     # 退出程序，正常退出时exit(0)
#sys.version     # 获取Python解释程序的版本信息
#sys.maxint      # 最大的Int值
#sys.maxunicode  # 最大的Unicode值
#sys.path        # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
#sys.platform    # 返回操作系统平台名称
#sys.stdout.write('please:')
#val = sys.stdin.readline()[:-1]
#print(val)

# os模块
# import os
# # 获取当前工作目录，即当前python脚本工作的目录路径
# os.getcwd()
# # 改变当前脚本工作目录；相当于shell下cd
# os.chdir("dirname")
# # 返回当前目录: ('.')
# os.curdir
# # 获取当前目录的父目录字符串名：('..')
# os.pardir
# # 可生成多层递归目录
# os.makedirs('dirname1/dirname2')
# # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.removedirs('dirname1')
# # 生成单级目录；相当于shell中mkdir dirname
# os.mkdir('dirname')
# # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.rmdir('dirname')
# # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.listdir('dirname')
# # 删除一个文件
# os.remove()
# # 重命名文件/目录
# os.rename("oldname","newname")
# # 获取文件/目录信息
# os.stat('path/filename')
# # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.sep
# # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.linesep
# # 输出用于分割文件路径的字符串
# os.pathsep
# # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.name
# # 运行shell命令，直接显示
# os.system("bash command")
# # 获取系统环境变量
# os.environ
# # 返回path规范化的绝对路径
# os.path.abspath(path)
# # 将path分割成目录和文件名二元组返回
# os.path.split(path)
# # 返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.dirname(path)
# # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.basename(path)
# # 如果path存在，返回True；如果path不存在，返回False
# os.path.exists(path)
# # 如果path是一个存在的文件，返回True。否则返回False
# os.path.isabs(path)
# # 如果path是一个存在的文件，返回True。否则返回False
# os.path.isfile(path)
# # 如果path是一个存在的目录，则返回True。否则返回False
# os.path.isdir(path)
# # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.join(path1[, path2[, ...]])
# # 返回path所指向的文件或者目录的最后存取时间
# os.path.getatime(path)
# # 返回path所指向的文件或者目录的最后修改时间
# os.path.getmtime(path)