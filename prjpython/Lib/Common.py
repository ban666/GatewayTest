# -*- coding:utf-8 -*-
__author__ = 'Ban'

import os,time,sys,glob
import xlsxwriter,xlrd

def judgeCaseLevel(case,level):
    caselevel=case[2]
    if caselevel in level:
        return 1
    else:
        return 0

def getTime_s():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())

def printCaseStart(case):
    msg="TestcaseNo.:"+case[0]+' Start'
    msg+=' TestcaseName:'+case[1]+' TestcaseLevel:'+case[2]+""
    return msg

def printCaseEnd(case):
    msg="TestcaseNo.:"+case[0]+' End'
    return msg

def getLogfile(fname):
    Nowtime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    Newname=''.join([os.path.split(fname)[0].replace('Scripts','Log'),'/','Log_',Nowtime,'.log'])
    return Newname

def getReportfile(fname):
    Nowtime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    Newname=''.join([os.path.split(fname)[0].replace('Scripts','Log'),'/','Report_',Nowtime,'.log'])
    return Newname

def getAllPy(folder):
    tstr=folder+"\\*.py"
    delstr=folder+"\\__init__.py"
    fileList=glob.glob(tstr)
    try:
        fileList.remove(delstr)
    except Exception as e:
        pass
    return fileList

def updateGlobal(fname,LogFile='',ReportFile='',TestLevel=['level 1','level 2','level 3','level 4','level 5'],*args):
    with open(fname,'w+') as f:
        tstr='Logfile='+'\''+LogFile+'\''+'\n'        
        f.write(tstr)
        tstr='ReportFile='+'\''+ReportFile+'\''+'\n'           
        f.write(tstr)
        tlist='['
        for i in TestLevel:
            tlist+='\''+i+'\''+','
        tlist=tlist.rstrip(',')
        tlist+=']'
        tstr='TestLevel='+tlist+'\n'           
        f.write(tstr)
        for i in args:
            tstr=i[0]+'='+'\''+i[1]+'\''+'\n'   
            f.write(tstr)

def setTcStatus(tcno,status):
    if status==0:
        result='FAILED'
    elif status==1:
        result='PASS'
    else:
        result='BLOCK'
    msg="TestcaseNo.:"+tcno+' result:'+result+""
    return msg

def reportMsgGenerate(logf,runtime):
    pcount=0
    fcount=0
    bcount=0
    count=0
    msg=''
    with open(logf,'r+') as f:
        for i in f:
            if i.find('result:')!=-1:
                count+=1
                treslut=i[i.find('result:')+7:].strip()
                if treslut=='PASS':
                    pcount+=1
                elif treslut=='FAILED':
                    fcount+=1
                elif treslut=='BLOCK':
                    bcount+=1
                else:
                    bcount+=1
    rate="%.2f%%" % (float(pcount)/float(count)*100)
    rtime="%.2f" % runtime
    rtime=secondsToTime(float(rtime))
    msg='本轮测试共运行测试用例'+str(count)+'个,共计用时:'+str(rtime[0])+'时'+str(rtime[1])+'分'+str(rtime[2])+'秒,其中PASS:'+str(pcount)+'个,FAILED:'+str(fcount)+'个,BLOCK:'+str(bcount)+'个,通过率:'+str(rate)
    return msg

def secondsToTime(iItv):

    if type(iItv)==type(0.1):
        h=int(iItv/3600)
        sUp_h=int(iItv-3600*h)
        m=sUp_h/60
        sUp_m=iItv-3600*h-60*m
        s=sUp_m
        tlist=[str(h),str(m),str(s)]
        return tlist
    else:
        return "[InModuleError]:itv2time(iItv) invalid argument type"

def generate_report(fname,sn,login_result,version_check_result,status_check_result,control_test_result,env_clear_result,case_result,s_time,e_time):
    result_dict = {1:'OK',0:'Failed',-1:'Block'}
    data = [login_result,version_check_result,status_check_result,control_test_result,env_clear_result,case_result]
    data = [result_dict[x] for x in data]
    data.insert(0,sn)
    data.append(s_time)
    data.append(e_time)
    ExcelWriteForAna(fname,data)

def ExcelWriteForAna(fname,content):
    if not os.path.exists(fname):
        xlsxwriter.Workbook(fname)
    columnlist=[u'网关sn',u'登录测试',u'版本检查测试',u'状态信息测试',u'控制测试',u'环境恢复',u'测试结果',u'开始时间',u'结束时间']
    data = xlrd.open_workbook(fn)            # 打开fname文件
    data.sheet_names()                          # 获取xls文件中所有sheet的名称
    table = data.sheet_by_index(0)              # 通过索引获取xls文件第0个sheet
    nrows = table.nrows                         # 获取table工作表总行数
    ncols = table.ncols
    tlist = []
    for i in xrange(nrows):              #设定第i行单元格属性，高度为22像素，行索引从0开始
        tlist.append([])
        for j in  xrange(ncols):
            tlist[i].append(table.cell_value(i,j,))
    tlist.append(content)
    if len(tlist)>1:
        tlist = tlist[1:]
    print tlist
    wb = xlsxwriter.Workbook(fname)
    ws = wb.add_worksheet()
    ws.set_column(0,8,22)
    #column
    for i in range(9):
        ws.write(0,i,columnlist[i])
    if tlist is not None:
        for i in range(len(tlist)):
            for j in range(9):
                ws.write(i+1,j,str(tlist[i][j]).decode('utf-8'))

    wb.close()

if __name__ == '__main__':
    fn = 'e:/3.xlsx'
    st = '2015-11-18 16:24:49'
    et = '2015-11-18 16:26:52'
    generate_report(fn,123,1,1,0,-1,-1,0,st,et)
    data = xlrd.open_workbook(fn)            # 打开fname文件
    data.sheet_names()                          # 获取xls文件中所有sheet的名称
    table = data.sheet_by_index(0)              # 通过索引获取xls文件第0个sheet
    nrows = table.nrows                         # 获取table工作表总行数
    ncols = table.ncols                         # 获取table工作表总列数
    print nrows
