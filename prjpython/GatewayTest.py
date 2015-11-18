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
        self.shuangkai_mac = self.cfg[4]
        self.sankai_mac = self.cfg[5]
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
        print self.shuangkai_mac,self.sankai_mac
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
            time.sleep(10)
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

            #env init
            try:
                al.clear_area(self.driver)
                al.clear_device(self.driver)
            except:
                pass
            #Get gateway version             
            version_content = al.get_version(self.driver)
            log.WritetoLog(self.logfile,'Get_version_result:'+str(version_content))
            if self.gateway_version == version_content:
                self.version_check_result = 1
            assert self.version_check_result == 1


            #add area
            area_list = ['Test']
            add_area_result  = al.add_area(self.driver,area_list)
            log.WritetoLog(self.logfile,'Add_area_result:'+str(add_area_result))
            assert add_area_result == 1

            #add device to areas
            device_list = [[self.shuangkai_mac,'1','2'],[self.sankai_mac,'2','1']]
            add_device_result  = al.add_devices(self.driver,device_list)
            log.WritetoLog(self.logfile,'Add_device_result:'+str(add_device_result))
            assert add_device_result == 1
            '''
            #wait for device

            msg = 'Please wait 2 minutes'
            log.WritetoLog(self.logfile,msg)
            al.wait_for_access(self.driver)
            #time.sleep(120)
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
            assert control_test_result == 1
            commit = raw_input('请确认开关是否控制成功：1、成功 2：失败'.decode('utf-8').encode('gbk'))
            if str(commit) == '1':
                self.control_test_result = 1
            else:
                self.control_test_result = 0
            assert self.control_test_result == 1

            TcStatus=1
        except Exception as e:
            msg= 'Error occurred:'+str(e)
            log.WritetoLog(self.logfile,msg)
        finally:
            #teardown
            try:
                #clear area
                clear_area_result  = al.clear_area(self.driver)
                log.WritetoLog(self.logfile,'Clear_area_result:'+str(clear_area_result))
                assert clear_area_result == 1
                #clear device
                clear_device_result  = al.clear_device(self.driver)
                log.WritetoLog(self.logfile,'Clear_device_result:'+str(clear_device_result))
                assert clear_device_result == 1
                

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

a=GatewayTest()
a.start_test()