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
from pc import pcMgr
from tdx import stockListWin, tdxOperator
from winsofts import webChatMgr

CaseInfo = {
    1:'近一个月中强势，30分钟信号线红，今天1分钟信号线已变红，注意看1分钟走势图中信号线是否在一买位置附近刚变红',
    2:'10天强势，今天1分钟信号线已变红，注意看1分钟走势图中信号线是否在一买位置附近刚变红'
}

webchat = webChatMgr.WebChatManager()

def heart_beat(str):
    print(str)
    chat = webChatMgr.WebChatManager()
    while 1:
        time.sleep(55)
        chat.send_heartbeat()
        if int(time.strftime("%H%M%S")) >= 150100 :
            pcMgr.ShutDown(2)
            

def StartTasks():
    t1 = threading.Thread(target=heart_beat,args=(u'heartbeat',))
    t1.start()

def SendStocksInfo(msg, images):
    # webchat.SendToGroup(msg, '')
    webchat.send_image_by_file_helper(msg, '')

    print(msg)
    for key, values in  images.items():
        print("%s:%s"%(key, values))
        webchat.send_image_by_file_helper(key, values)
        # webchat.SendToGroup(key, image)
        time.sleep(0.5)

def BeginSelectStockTask(tdx, caseIndex=1):
    if caseIndex < 1 or caseIndex > 2:
        return

    result = tdx.DoSelectStocksNow(caseIndex)
    stocksWin = stockListWin.StockListWin()
    if result > 0:
        tdx.AddTempStocksToSelfChoose(result)
    images = {}
    images = tdx.CaptureStocksDrawings(result, stocksWin)
    SendStocksInfo(CaseInfo[caseIndex], images)
    tdx.SwitchToSelfChooseMainFrame()

def MonitorSelfChooseStocks(tdx):
    tdx.SwitchToSelfChooseMainFrame()
    tdx.SyncSelfChoose()

    current = stockListWin.StockListWin(u'行情报价-自选股')
    stocks = current.CountList()
    number = len(stocks)
    print('自选股数 %d'%number)
    
    images = {}
    images = tdx.CaptureStocksDrawings(number, current)
    SendStocksInfo('自选股监控', images)
    time.sleep(5)
        
if __name__=='__main__':
    
    StartTasks()
    time.sleep(5)

    tdx = tdxOperator.TdxOperator()
    tdx.OpenTdx()
    
    while 1:
        currentTime = int(time.strftime("%H%M%S"))
        if currentTime >= 93000 :

            time.sleep(10)

            tdx.SwitchToSelfChooseMainFrame()
            MonitorSelfChooseStocks(tdx)
            
            tdx.UpdataRealTimeData()
            if  (currentTime > 113000 and currentTime < 130000) or (currentTime > 153000):
                BeginSelectStockTask(tdx, 1)    
            else:
                BeginSelectStockTask(tdx, 2) 
               
            time.sleep(30)

            tdx.SwitchToSelfChooseMainFrame()      
        else:
            print("time to sleep")
            time.sleep(2)
