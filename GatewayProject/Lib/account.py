#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-11-06 09:24:41
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-17 11:15:03

import urllib  
import urllib2
import json
import sys  
import cookielib  
from urllib2 import URLError  




def http_post(url,data,headers):
    jdata = urllib.urlencode(data)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata, headers)       # 生成页面请求的完整数据
    response = urllib2.urlopen(req)       # 发送页面请求
    return response.read()                    # 获取服务器返回的页面信息

def create_user(sn,password='123456'):
    #head
    ExploereHEADERS = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Content-Length':'96',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'JSESSIONID=8DAD5F49CA51DD5558B7574AE9BB84FB',
        'Host':'59.175.180.10:8080',
        'Origin':'http://59.175.180.10:8080',
        'Referer':'http://59.175.180.10:8080/SmartHomeManage/janlinker/user/createUser.jsp',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
    }   
    url = 'http://59.175.180.10:8080/SmartHomeManage/janlinker/createUser'
    username = sn+'test'
    password = '123456'
    data = {
        'sSN':sn,
        'sRemark':sn,
        'sTel':'13411111111',
        'name':sn+'test',
        'password':'123456',
        'rePassword':'123456',
        'type':'4'
    }
    #设置cookie  
    cj = cookielib.CookieJar()  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
    # 安装cookie  
    urllib2.install_opener(opener)   
    try:
        http_post(url,data,ExploereHEADERS)
        result = [username,password]
        return result
    except Exception as e:
        print e

