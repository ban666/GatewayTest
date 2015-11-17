# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 09:57:26
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-05 10:38:48

import sys,os,time

sys.path.append("../../Lib/")
sys.path.append("../../GlobalInfo/")
import configrw as cf
import Common as Common
import loglib as log
import GlobalInfo as Global
import Mobileinfo as Mb
import appium_lib as al
from appium import webdriver
import time
#readcfg


class GatewayTest:

    def __init__(self):
        self.cfg=cf.readcfg(__file__)
        logfile= Global.Logfile
        print self.cfg
        '''
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
            area_list = ['abc','def']
            add_area_result  = al.add_area(driver,area_list)
            log.WritetoLog(logfile,'Add_area_result:'+str(add_area_result))
            assert add_area_result == 1
            del_area_result  = al.del_area(driver,area_list)
            log.WritetoLog(logfile,'Del_area_result:'+str(del_area_result))
            assert del_area_result == 1
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
        '''

a=GatewayTest()