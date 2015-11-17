#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-04-14 09:23:40
# @Last Modified by:   liaoben
# @Last Modified time: 2015-10-27 14:35:46

import sys,os,time

sys.path.append("../Lib/")
sys.path.append("../GlobalInfo/")
import configrw as cf
import Common as Common
import loglib as log
import GlobalInfo as Global
#readcfg
cfg=cf.readcfg(__file__)
logfile= Global.Logfile

for case in cfg:
    try:
        #set up
        TcStatus=0
        msg=Common.printCaseStart(case)
        log.WritetoLog(logfile,msg)
        #test
        
        
    except Exception as e:
        msg= 'Error occurred:'+e
        log.WritetoLog(logfile,msg)
    finally:
        #teardown
        msg=Common.printCaseEnd(case)
        log.WritetoLog(logfile,msg)
        