# -*- coding:utf-8 -*-
__author__ = 'Ban'

import sys,os,time
sys.path.append("../Lib")
import configrw
import loglib
#readcfg
cfg=configrw.readcfg(__file__)
#Log Settings
logfile=loglib.GetLogfile(__file__)


for case in cfg:
    try:
        print 2222222222222
        msg=loglib.Printcase(case)
        loglib.WritetoLog(logfile,msg)
    except Exception as e:
        print 'Error:',e
    finally:
        pass