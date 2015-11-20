# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 09:57:26
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-18 15:31:02

import sys,os,time

import Lib.configrw as cf
import Lib.Common as Common
import Lib.loglib as log
from GlobalInfo import Logfile,ReportFile 
import Lib.appium_lib as al
from GlobalInfo.Mobileinfo import desired_caps
import Lib.account as account
from appium import webdriver
import time
#readcfg


class GatewayTest:

    def __init__(self,case):
        self.logfile= Logfile
        self.report = ReportFile
        self.gateway_version = case[0]
        self.sn = case[1]
        self.light_result = 2
        self.shuangkai_mac = case[2]
        self.sankai_mac = case[3]
        self.desired_caps = desired_caps
        self.login_result = -1
        self.version_check_result = -1
        self.status_check_result = -1
        self.control_test_result = -1
        self.env_clear_result = -1

    def start_test(self):
        #set up
        TcStatus=0
        msg='测试开始...'
        s_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log.WritetoLog(self.logfile,msg)
        #test
        try:
            #set up
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            time.sleep(8)
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
            self.login_result = al.login_to_page(self.driver,self.username,self.password,self.sn)
            log.WritetoLog(self.logfile,'Login_result:'+str(self.login_result))
            assert self.login_result == 1
            time.sleep(5)

            #Get gateway version             
            version_content = al.get_version(self.driver)
            log.WritetoLog(self.logfile,'Get_version_result:'+str(version_content))
            if self.gateway_version == version_content:
                self.version_check_result = 1
            assert self.version_check_result == 1

            #add area and devices
            area = 'Test'
            device_list = [[self.shuangkai_mac,'1','2'],[self.sankai_mac,'2','1']]
            add_device_result = al.add_area_devices(self.driver,area,device_list)
            assert add_device_result == 1

            '''
            #wait for device
            msg = 'Please wait 2 minutes'
            log.WritetoLog(self.logfile,msg)
            al.wait_for_access(self.driver)
            #time.sleep(120)
            '''
            '''
            #status check
            light_control_result  = al.get_all_opendevice_in_light(self.driver)
            if len(light_control_result) == 1 and light_control_result[0] == self.light_result:
                self.status_check_result = 1
            else:
                self.status_check_result = 0
            log.WritetoLog(self.logfile,'status_check_result:'+str(self.status_check_result))
            assert self.status_check_result == 1

            #control test
            control_test_result = al.control_device_in_device(self.driver)
            log.WritetoLog(self.logfile,'Control_test_result:'+str(control_test_result))
            self.control_test_result = control_test_result
            assert self.control_test_result == 1
            '''
            TcStatus=1
        except Exception as e:
            msg= 'Error occurred:'+str(e)
            log.WritetoLog(self.logfile,msg)
            self.driver.quit()
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            time.sleep(5)
            self.login_result = al.login_to_page(self.driver,self.username,self.password,self.sn)
        finally:
            #teardown
            try:
                clear_env_result  = al.clear_env(self.driver)

                log.WritetoLog(self.logfile,'环境恢复成功！')
            except Exception as e:
                print e
                log.WritetoLog(self.logfile,'环境恢复失败！')
            finally:
                self.driver.quit()

            msg='测试结果:'+str(TcStatus) #Set Result
            log.WritetoLog(self.logfile,msg)             
            msg='测试结束...'
            log.WritetoLog(self.logfile,msg) 
            e_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #generate report
            Common.generate_report(self.report,self.sn,self.login_result,self.version_check_result,self.status_check_result,self.control_test_result,self.env_clear_result,TcStatus,s_time,e_time)

cases = cf.get_case(__file__)
for case in cases:
    a=GatewayTest(case)
    a.start_test()