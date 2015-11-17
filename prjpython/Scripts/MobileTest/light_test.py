#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 09:57:26
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-09 11:33:27

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
#cfg=cf.readcfg(__file__)
#logfile= Global.Logfile
try:
    #set up
    TcStatus=0
    username='zzh'
    password='123456'
    sn ='01379426'
    #test
    try:
        #set up
        driver = webdriver.Remote('http://localhost:4723/wd/hub', Mb.desired_caps)
        time.sleep(5)
        #test
        login_result = al.login_to_page(driver,username,password,sn)
        assert login_result == 1
        time.sleep(5)
        light_control_result  = al.get_all_opendevice_in_light(driver)
        if len(light_control_result) == 1 and light_control_result[0] == self.light_result:
            status_check_result = 1
        else:
            status_check_result = 0
        assert status_check_result == 1
    except Exception as e:
        msg= 'Error occurred:'+str(e)
    finally:
        #teardown
        try:
            driver.quit()
        except:
            pass #Set Result
        log.WritetoLog(logfile,msg)
        msg=Common.printCaseEnd(case) 
        log.WritetoLog(logfile,msg)
except Exception as e :
    print e