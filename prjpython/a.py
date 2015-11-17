#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-11-17 14:09:26
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-17 14:11:13

url = 'http://59.175.180.10:8080/SmartHomeManage/janlinker/createUser'
sn='01309196'
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

url= url+'?'
for i,j in data.items():
    url =url+i+'='+j+'&'
print url