# -*- coding: UTF-8 -*-

import datetime
import sys
import threading
import time
from win32.lib import win32con
import win32api
import win32gui
import win32process
import win32ui

from winsofts import webchat
from pc import pcMgr
from tdx import stockListWin, tdxOperator


CaseInfo = {
    1:'近一个月中强势，30分钟信号线红，今天1分钟信号线已变红，注意看1分钟走势图中信号线是否在一买位置附近刚变红',
    2:'10天强势，今天1分钟信号线已变红，注意看1分钟走势图中信号线是否在一买位置附近刚变红'
}

 
def heart_beat(str):
    print(str)
    while 1:
        msg = "heartbeat %s"%(time.strftime("%H:%M:%S"))
        webchat.send_msg_to_friend(msg)
        cur = int(time.strftime("%H%M%S"))
        if cur >= 150100 and cur < 160000:
            pcMgr.ShutDown(2)
        time.sleep(5*60)
            

def StartTasks():
    t1 = threading.Thread(target=heart_beat,args=(u'heartbeat',))
    t1.start()

def BeginSelectStockTask(tdx, caseIndex=1):
    if caseIndex < 1 or caseIndex > 2:
        return
    result = tdx.DoSelectStocksNow(caseIndex)
    stocksWin = stockListWin.StockListWin()
    if result > 0:
        tdx.AddTempStocksToSelfChoose(result)
    webchat.send(CaseInfo[caseIndex])
    tdx.CaptureStocksDrawings(result, stocksWin)
    tdx.SwitchToSelfChooseMainFrame()

def MonitorSelfChooseStocks(tdx):
    tdx.SwitchToSelfChooseMainFrame()
    tdx.SyncSelfChoose()
    current = stockListWin.StockListWin(u'行情报价-自选股')
    stocks = current.CountList()
    number = len(stocks)
    print('自选股数 %d'%number)
    msg = '自选股监控 %s'%(time.strftime("%H:%M:%S"))
    webchat.send(msg)
    tdx.CaptureStocksDrawings(number, current)
     
    time.sleep(5)

def CalcSleepTime(currentTime):
    sleeptime = 1
    if  (currentTime > 113000 and currentTime < 130000):
        sleeptime = 130000-int(time.strftime("%H%M%S"))
    elif currentTime > 150000:
        sleeptime = int(time.strftime("%H%M%S"))-130000
    return sleeptime
        
if __name__=='__main__':
    
    webchat.login()
     
    StartTasks()
    time.sleep(10)

    tdx = tdxOperator.TdxOperator()
    tdx.OpenTdx()
    tdx.SwitchToSelfChooseMainFrame()

    while 1:
        currentTime = int(time.strftime("%H%M%S"))
        if currentTime >= 93000 :

            tdx.SwitchToSelfChooseMainFrame()

            MonitorSelfChooseStocks(tdx)
            tdx.UpdataRealTimeData()
            BeginSelectStockTask(tdx, 1)  
            BeginSelectStockTask(tdx, 2) 

            time.sleep(CalcSleepTime(currentTime))
        else:
            print("time to sleep")
            time.sleep(2)
