#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-04-14 10:29:06
# @Last Modified by:   liaoben
# @Last Modified time: 2015-04-16 14:25:40

import os,sys,re

def reportMsgGenerate(logf):
    pcount=0
    fcount=0
    bcount=0
    count=0
    msg=''
    with open(logf,'r+') as f:
        for i in f:
            if i.find('result:')!=-1:
                count+=1
                treslut=i[i.find('result:')+7:].strip()
                if treslut=='PASS':
                    pcount+=1
                elif treslut=='FAILED':
                    fcount+=1
                elif treslut=='BLOCK':
                    bcount+=1
                else:
                    bcount+=1
    rate="%.2f%%" % (float(pcount)/float(count)*100)
    msg='本轮测试共运行测试用例'+str(count)+'个,其中PASS:'+str(pcount)+'个,FAILED:'+str(fcount)+'个,BLOCK:'+str(bcount)+'个,通过率:'+str(rate)
    return msg

from pylab import *

n = 20
Z = np.random.uniform(0,1,n)
Z=array([0,100,0])
pie(Z), show()