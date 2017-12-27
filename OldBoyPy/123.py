#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import json
#import urllib, urllib2

'''
def getulr(url):
    req = urllib2.Request(url)
    res = json.loads(urllib2.urlopen(req).read())
    return req
myurl = sys.argv[1]
print(myurl)
print(123)
'''
import json
name_dic = {'name': 'yinxl', 'age': '23'}
print(json.dumps(name_dic), type(json.dumps(name_dic)))
print(json.loads(json.dumps(name_dic)), type(json.dumps(name_dic)))
a = name_dic['name']
print(a)