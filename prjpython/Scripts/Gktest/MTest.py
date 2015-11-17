# -*- coding:utf-8 -*-
__author__ = 'Ban'

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
    if not Common.judgeCaseLevel(case,Global.TestLevel):
        continue
    try:
        #set up
        TcStatus=0 #Init Result
        msg=Common.printCaseStart(case)
        log.WritetoLog(logfile,msg)

        #test begin:
        TcStatus=1
        
        
    except Exception as e:
        #Error
        msg= 'Error occurred:'+e
        log.WritetoLog(logfile,msg)
    finally:
        #teardown
        msg=Common.setTcStatus(case[0],TcStatus) #Set Result
        log.WritetoLog(logfile,msg)
        msg=Common.printCaseEnd(case) 
        log.WritetoLog(logfile,msg)

