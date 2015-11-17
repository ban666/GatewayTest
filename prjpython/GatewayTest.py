# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 09:57:26
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-17 15:45:47

import sys,os,time

import Lib.configrw as cf
import Lib.Common as Common
import Lib.loglib as log
from GlobalInfo import Logfile,ReportFile 
import Lib.appium_lib as al
import Lib.account as account
from appium import webdriver
import time
#readcfg


class GatewayTest:

    def __init__(self):
        self.cfg=cf.readcfg(__file__)
        self.logfile= Logfile
        self.report = ReportFile
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
        self.login_result = -1
        self.version_check_result = -1
        self.status_check_result = -1
        self.control_test_result = -1
        self.env_clear_result = -1

    def start_test(self):
        #set up
        TcStatus=0
        msg='测试开始...'.decode('utf-8')
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
            self.username = 'zzh'
            self.password = '123456'

            #Login
            self.login_result = al.login_to_page(driver,self.username,self.password,self.sn)
            log.WritetoLog(self.logfile,'Login_result:'+str(self.login_result))
            assert self.login_result == 1
            time.sleep(5)

            #Get gateway version             
            version_content = al.get_version(driver)
            log.WritetoLog(self.logfile,'Get_version_result:'+str(version_content))
            assert version_content[0] == 1             
            print 'gateway_version:',version_content[1]
            if self.gateway_version == version_content[1]:     
                self.version_check_result = 1
            assert self.version_check_result == 1


            #add area
            area_list = ['abc']
            add_area_result  = al.add_area(driver,area_list)
            log.WritetoLog(self.logfile,'Add_area_result:'+str(add_area_result))
            assert add_area_result == 1

            #add device to areas

            #status check
            light_control_result  = al.get_all_opendevice_in_light(driver)
            if len(light_control_result) == 1 and light_control_result[0] == self.light_result:
                self.status_check_result = 1
            else:
                self.status_check_result = 0
            log.WritetoLog(self.logfile,'Light_control_result:'+str(self.status_check_result))
            assert self.status_check_result == 1

            #control test
            control_test_result = al.control_device_in_device(driver)
            log.WritetoLog(self.logfile,'Control_test_result:'+str(control_test_result))
            assert control_test_result == 1
            commit = raw_input('请确认开关是否控制成功：1、成功 2：失败'.decode('utf-8'))
            if commit == '1':
                self.control_test_result = 1
            else:
                self.control_test_result = 0
            assert self.control_test_result = 1

            TcStatus=1
        except Exception as e:
            msg= 'Error occurred:'+str(e)
            log.WritetoLog(self.logfile,msg)
        finally:
            #teardown
            try:
                #clear area
                clear_area_result  = al.clear_area(driver)
                log.WritetoLog(self.logfile,'Clear_area_result:'+str(clear_area_result))
                assert del_area_result == 1

                #clear device
                clear_device_result  = al.clear_device(driver,len(area_list))
                log.WritetoLog(self.logfile,'Clear_device_result:'+str(clear_device_result))
                assert clear_device_result == 1
                driver.quit()
                log.WritetoLog(self.logfile,'环境恢复成功！'.decode('utf-8'))
            except:
                log.WritetoLog(self.logfile,'环境恢复失败！'.decode('utf-8'))
            msg='测试结果:'+str(TcStatus) #Set Result
            log.WritetoLog(self.logfile,msg)             
            msg='测试结果...'.decode('utf-8')
            log.WritetoLog(self.logfile,msg) 

            #generate report
            Common.generate_report(self.report,self.sn,self.login_result,self.version_check_result,self.status_check_result,self.control_test_result,self.env_clear_result,TcStatus)        

a=GatewayTest()
a.start_test()