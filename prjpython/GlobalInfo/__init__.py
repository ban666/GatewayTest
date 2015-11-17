__author__ = 'Administrator'

import time
import os
nowTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
dirname = os.path.dirname(os.path.abspath(__file__))
Logfile = dirname.replace('GlobalInfo','Log/')+'Log_'+nowTime+'.log'
ReportFile=dirname.replace('GlobalInfo','Log/')+'Report_'+nowTime+'.xlsx'
TestLevel=['level 1','level 2','level 3','level 4','level 5']

def gen_file(fn):
    with open(fn,'w+') as f:
        pass
gen_file(Logfile)
gen_file(ReportFile)