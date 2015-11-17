# -*- coding:utf-8 -*-
__author__ = 'Ban'

import sys,os,time,glob,subprocess
sys.path.append("../Lib")
sys.path.append('../GlobalInfo')
import Common,GlobalInfo,configrw,loglib,maillib
import mailinfo as m

def testa():
    GlobalFile= os.getcwd().replace('Scripts','GlobalInfo')+'\\GlobalInfo.py'
    ReportFile=Common.getReportfile(__file__)
    Log=Common.getLogfile(__file__)
    lista=[GlobalFile,Log,ReportFile]
    return lista

def excuteCaseSuite(folderlist):
    for j in folderlist:
        ExcutePath=os.getcwd()+"\\"+j
        fileList=Common.getAllPy(ExcutePath)
        for i in fileList:
            os.system(i)

#Global Settings
level=['level 1','level 2','level 3','level 4','level 5']
result=testa()
Common.updateGlobal(result[0],LogFile=result[1],ReportFile=result[2],TestLevel=level)
#set Excute case
time_start=time.time()
Case=['Gktest']
excuteCaseSuite(Case)
time_end=time.time()
excutetime=time_end-time_start
#Report Analysis
msg_result=Common.reportMsgGenerate(result[1],excutetime)
loglib.WritetoLog(result[1],msg_result)
#Send Email
'''
toAdd = ['liaob@janlinker.com']
subject = '自动化测试报告_'+Common.getTime_s()
plainText = msg_result
htmlText = ''
attfile = 'E:\\Program Files (x86)\\JetBrains\\PyCharm 3.4.1\\jre\\jre\\bin\\e\\work\\Zigbeetest\\Analysis/Zipfile/20150615110540.zip'
mailresult=maillib.sendEmail(m.server,m.user,m.password, m.fromAdd, toAdd, subject, plainText, htmlText,attfile)
if not mailresult:
    print mailresult
'''