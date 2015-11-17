#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 10:00:37
# @Last Modified by:   liaoben
# @Last Modified time: 2015-10-27 10:06:01
import os
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Nexus_7_2012_API_19'
#desired_caps['appPackage'] = 'com.jlkj.janlinker'
#desired_caps['appActivity'] = 'com.jlkj.janlinker/com.jlkj.janlinker.ui.SplashActivity'
PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)
desired_caps['app'] = PATH('C:\\Users\\Administrator\\Desktop\\Janlinker.apk')#被测试的App在电脑上的位置
#driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
