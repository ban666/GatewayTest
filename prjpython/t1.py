# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 09:57:26
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-17 14:43:13

import sys,os,time

import Lib.configrw as cf
import Lib.Common as Common
import Lib.loglib as log
from GlobalInfo import Logfile 
import Lib.appium_lib as al
import Lib.account as account
from appium import webdriver
import time
#readcfg


class GatewayTest:

    def __init__(self):
        self.cfg=cf.readcfg(__file__)
        self.logfile= Logfile
        self.app = self.cfg[0]
        self.gateway_version = self.cfg[1]
        self.sn = self.cfg[2]
        self.light_result = self.cfg[3]
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '4.4.2'
        self.desired_caps['deviceName'] = 'Nexus_7_2012_API_19'
        PATH=lambda p:os.path.abspath(
        os.path.join(os.path.dirname(__file__),p)                            
        )
        self.desired_caps['app'] = PATH(self.app)
        print self.logfile

    def start_test(self):
        #set up
        TcStatus=0
        msg='Start Test...'
        log.WritetoLog(self.logfile,msg)
        #test
        try:
            #set up
            driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            time.sleep(5)
            #test
            #registry
            '''
            registry_result = account.create_user(self.sn)
            self.username = registry_result[0]
            self.password = registry_result[1]
            '''
            self.username = 'b'
            self.password = '123456'
            #Login
            login_result = al.login_to_page(driver,self.username,self.password,self.sn)
            log.WritetoLog(self.logfile,'Login_result:'+str(login_result))
            assert login_result == 1
            time.sleep(5)

            al.clear_area(driver)
            #al.clear_device(driver)
            
            TcStatus=1
        except Exception as e:
            msg= 'Error occurred:'+str(e)
            log.WritetoLog(self.logfile,msg)
        finally:
            #teardown
            try:
                driver.quit()
            except:
                pass
            msg='Test Result:'+str(TcStatus) #Set Result
            log.WritetoLog(self.logfile,msg)             
            msg='End Test...'

a=GatewayTest()
a.start_test()