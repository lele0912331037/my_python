#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib,urllib2
import json
class weChat:
    def __init__(self,url,Corpid,Secret):
        url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url,Corpid,Secret)
        res = self.url_req(url)
        self.token = res['access_token']
    def url_req(self,url,method='get',data={}):
        if method == 'get':
            req = urllib2.Request(url)
            res = json.loads(urllib2.urlopen(req).read())
        elif method == 'post':
                        req = urllib2.Request(url,data)
                        res = json.loads(urllib2.urlopen(req).read())
        else:
            print 'error request method...exit'
            sys.exit()
        return res
    def send_message(self, content, agentid=0, userlist=''):
        self.userlist = userlist
        self.content = content
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % self.token
        data = {
                      "touser": "",
                      "toparty": "",
                      "totag": "",
                      "msgtype": "text",
                      "agentid": "0",
                      "text": {
                          "content": ""
                      },
                      "safe":"0"
                   }
        data['touser'] = userlist
        data['agentid'] = agentid
        data['text']['content'] = content
        data = json.dumps(data,ensure_ascii=False)
    #   print data
        res = self.url_req(url,method='post',data=data)
        if res['errmsg'] == 'ok':
            print 'send sucessed!!!'
        else:
            print 'send failed!!'
            print res

if __name__ == '__main__':
      #userlist = sys.argv[1]
      content = sys.argv[1:]
      content = '\n'.join(content)
      Corpid = 'wx0c3c45ee3195932a'
      Secret = 'UBCvh6yEuxrpEIbnbgFhyl9Xdx4SKHQ3TsofhCCe0QUqRqb6Zh90kDwqGolz1Rwu'
      url = 'https://qyapi.weixin.qq.com'
      wechat = weChat(url,Corpid,Secret)
      wechat.send_message(content,1000002)