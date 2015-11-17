#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 09:57:26
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-03 09:24:32

import sys,os,time
if __name__ == '__main__':
    sys.path.append("../../Lib/")
    sys.path.append("../../GlobalInfo/")
else:
    sys.path.append("../Lib/")
    sys.path.append("../GlobalInfo/")
import configrw as cf
import Common as Common
import loglib as log
import GlobalInfo as Global
import Mobileinfo as Mb
import appium_lib as al
from appium import webdriver
import time
#readcfg
cfg=cf.readcfg(__file__)
logfile= Global.Logfile

for case in cfg:
    if not Common.judgeCaseLevel(case,Global.TestLevel):
        continue
    #set up
    TcStatus=0
    msg=Common.printCaseStart(case)
    log.WritetoLog(logfile,msg)
    username=case[3]
    password=case[4]
    sn =case[5]
    #test
    try:
        #set up
        driver = webdriver.Remote('http://localhost:4723/wd/hub', Mb.desired_caps)
        time.sleep(5)
        #test
        login_result = al.login_to_page(driver,username,password,sn)
        log.WritetoLog(logfile,'Login_result:'+str(login_result))
        assert login_result == 1
        time.sleep(5)
        version_content = al.get_version(driver)
        log.WritetoLog(logfile,'Get_version_result:'+str(version_content))
        assert version_content[0] == 1
        print 'gateway_ver:',version_content[1],'software_ver',version_content[2]
        TcStatus=1
    except Exception as e:
        msg= 'Error occurred:'+str(e)
        log.WritetoLog(logfile,msg)
    finally:
        #teardown
        try:
            driver.quit()
        except:
            pass
        msg=Common.setTcStatus(case[0],TcStatus) #Set Result
        log.WritetoLog(logfile,msg)
        msg=Common.printCaseEnd(case) 
        log.WritetoLog(logfile,msg)
        