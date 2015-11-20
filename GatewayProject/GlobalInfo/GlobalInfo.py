import time
import os
nowTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
Logfile = os.getcwd().replace('GlobalInfo','Log/')+'Log_'+nowTime+'.log'
ReportFile=os.getcwd().replace('GlobalInfo','Log/')+'Report_'+nowTime+'.log'
#Logfile='E:\work\prjpython\Log/Log_20151027102457.log'
TestLevel=['level 1','level 2','level 3','level 4','level 5']

def gen_file(fn):
    with open(fn,'w+') as f:
        pass
gen_file(Logfile)
gen_file(ReportFile)
print Logfile