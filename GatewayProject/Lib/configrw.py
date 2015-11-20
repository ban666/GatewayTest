# -*- coding:utf-8 -*-
__author__ = 'Ban'

import ConfigParser,os


def readcfg(cfg,opt='info'):
    list1=[]
    cfg=''.join([cfg[:-2],'cfg'])
    config=ConfigParser.ConfigParser()
    with open(cfg,"r") as cfgfile:
        config.readfp(cfgfile)
        op=config.options(opt)
    for i in op:
        list1.append(config.get(opt,i))
    return list1

def updateGlobal(vallist,cfg=''):
    config=ConfigParser.ConfigParser()
    config.read(cfg)
    for val in valist:
        config.set('Global',val[0],val[1])
    config.write( open(cfg, 'r+') )

def get_case(fn):
    fn = '.'.join([os.path.splitext(fn)[0],'cfg'])
    with open(fn,'r+') as f:
        cases = list(f)
    cases=[x.strip() for x in cases[1:]]
    poplist = []
    for i in range(len(cases)):
        if cases[i].find('#')==0:
            poplist.append(i)
    for j in poplist[::-1]:
        cases.pop(j)
    cases = [x.split(',') for x in cases]
    return cases