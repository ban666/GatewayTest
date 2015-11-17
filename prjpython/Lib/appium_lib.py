#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: liaoben
# @Date:   2015-10-27 10:14:36
# @Last Modified by:   liaoben
# @Last Modified time: 2015-11-17 15:10:27

from appium import webdriver
import time,sys
def login(driver,username,password):
    result = -1
    try:
        uname = driver.find_element_by_id('com.jlkj.janlinker:id/et_username')
        pword = driver.find_element_by_id('com.jlkj.janlinker:id/et_password')
        login_button = driver.find_element_by_id('com.jlkj.janlinker:id/login')
        uname.send_keys(username)
        pword.send_keys(password)
        login_button.click()
        result = 1
    except Exception as e:
        print 'login_error:',e
        result = 0
    finally:
        return result

def select_sn(driver,sn):
    result = -1
    try:
        snlist = driver.find_elements_by_id('com.jlkj.janlinker:id/tv_number')
        for i in snlist:
            print i.text.encode('utf-8').decode('utf-8')
            if i.text.encode('utf-8').split('(')[1] == sn +')':
                i.click()
                time.sleep(2)
                result = 1
                break
        
    except Exception as e:
        print 'select_sn_error:',e
        result = 0
    finally:
        return result

def login_to_page(driver,username,password,sn):
    login_result = login(driver,username,password)
    if login_result != 1:
        return 0
    time.sleep(5)
    cur_activity=driver.current_activity
    if cur_activity=='.ui.MainActivity':
        try:
            driver.find_element_by_id('com.jlkj.janlinker:id/negativeButton').click()
        except:
            pass
        return login_result
    s_sn_result = select_sn(driver,sn)
    try:
        driver.find_element_by_id('com.jlkj.janlinker:id/negativeButton').click()
    except:
        pass
    return s_sn_result

#open_menu
#return_val:[status:1/-1,menu_content:type:list]
#menucontent[0]:主页
#menucontent[1]:视频监控
#menucontent[2]:告警信息
#menucontent[3]:日志管理
#menucontent[4]:系统设置
#menucontent[5]:系统服务
#menucontent[6]:关于本机
def open_menu(driver):
    result = -1
    try:
        menu = driver.find_element_by_id('com.jlkj.janlinker:id/iv_menu')
        menu.click()
        menu_content = driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')
        result = [1,menu_content]
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def get_version(driver):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_info = menu_result[1][-1].click()
        gwver = driver.find_element_by_id('com.jlkj.janlinker:id/txtgetgwVersion').text.encode('utf-8')
        softver = driver.find_element_by_id('com.jlkj.janlinker:id/txtgetSoftVersion').text.encode('utf-8')
        gateway_ver = gwver.split(':')[-1]
        software_ver = softver.split(':')[-1]
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = [1,gateway_ver[-5:],software_ver[-5:]]
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def clear_device(driver):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_info = menu_result[1][-2].click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/icondetail')[0].click()
        device_num = 0
        try:
            device_num = len(driver.find_elements_by_id('com.jlkj.janlinker:id/tv_mac'))
        except:
            pass
        for device in range(device_num):
            driver.swipe(810,150,110,160,1000);
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":845, "y":163})
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
            time.sleep(5)
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def add_area(driver,areas):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_settings = menu_result[1][4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        add_area = driver.find_elements_by_id('com.jlkj.janlinker:id/showpop')[0].click()
        for area in areas:
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":32, "y":448})
            area_name = driver.find_element_by_id('com.jlkj.janlinker:id/message').send_keys(area)
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":873, "y":100})
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def del_area(driver,areas_num):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_settings = menu_result[1][4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        add_area = driver.find_elements_by_id('com.jlkj.janlinker:id/showpop')[0].click()
        for area in range(areas_num):
            driver.swipe(810,150,110,160,1000);
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":845, "y":163})
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":873, "y":100})
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def clear_area(driver):
    result = -1
    try:
        menu_result = open_menu(driver)
        if menu_result[0] != 1:
            return 0
        sys_settings = menu_result[1][4].click()
        init_settings = driver.find_elements_by_id('com.jlkj.janlinker:id/textitem')[0].click()
        areas_num = len(driver.find_elements_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView'))
        add_area = driver.find_elements_by_id('com.jlkj.janlinker:id/showpop')[0].click()
        for area in range(areas_num):
            driver.swipe(810,150,110,160,1000);
            driver.execute_script("mobile: tap", {"touchCount":"1", "x":845, "y":163})
            driver.find_element_by_id('com.jlkj.janlinker:id/positiveButton').click()
        driver.execute_script("mobile: tap", {"touchCount":"1", "x":873, "y":100})
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_element_by_id('com.jlkj.janlinker:id/iv_back').click()
        driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')[0].click()
        result = 1
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def open_light_module(driver):
    result = -1
    try:
        driver.find_element_by_id('com.jlkj.janlinker:id/item_name')[0].click()
        menu.click()
        menu_content = driver.find_elements_by_id('com.jlkj.janlinker:id/tv_title')
        result = [1,menu_content]
    except Exception as e:
        func_name = sys._getframe().f_code.co_name
        print func_name+'_Error:',e
        result = 0
    finally:
        return result

def get_all_opendevice_in_light(driver):
    driver.find_elements_by_id('com.jlkj.janlinker:id/item_name')[1].click()
    c = driver.find_elements_by_android_uiautomator('new UiSelector().checked(true)')
    result = []
    for i in c:
        try:
            r='-1'
            txt = i.text.encode('utf-8')
            print txt.decode('utf-8')
            if txt == '①开':
                r = '1'
                result.append(r)
            elif txt == '②开':
                r = '2'
                result.append(r)
            elif txt == '③开':
                r = '3'
                result.append(r)
            print r
        except Exception as e :
            print e
    return result

def control_device_in_device(driver):
    driver.find_elements_by_id('com.jlkj.janlinker:id/item_name')[2].click()
    cb = driver.find_elements_by_class_name('android.widget.CheckBox')
    result = 1
    for i in cb:
        try:
            print i.text.encode('utf-8')
            i.click()
            result = result * 1
        except Exception as e :
            print e
            result = result * 0
            break
    return result