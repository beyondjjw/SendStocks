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
    for image in images:
        webchat.SendToGroup(msg, image)
        webchat.send_image_by_file_helper(msg, image)

def BeginSelectStockTask(tdx):
    caseIndex = 2
    result = 0
    while result <= 5 and caseIndex <= 2:
        result = tdx.DoSelectStocksNow(caseIndex)
        stocksWin = stockListWin.StockListWin()
        if result > 0:
            tdx.AddTempStocksToSelfChoose(result)
        images = []
        images = tdx.CaptureStocksDrawings(result, stocksWin)
        SendStocksInfo(CaseInfo[caseIndex], images)
        if result <= 5:
            caseIndex = 1
        else:
            break
        tdx.SwitchToSelfChooseMainFrame()
        
if __name__=='__main__':
    
    StartTasks()
    time.sleep(10)

    tdx = tdxOperator.TdxOperator()
    tdx.OpenTdx()
    
    while 1:
        
        if int(time.strftime("%H%M%S")) >= 93000 :
            # tdx = tdxOperator.TdxOperator()
            # tdx.OpenTdx()
            tdx.SwitchToSelfChooseMainFrame()
            tdx.SyncSelfChoose()

            current = stockListWin.StockListWin(u'行情报价-自选股')
            stocks = current.CountList()
            number = len(stocks)
            print('自选股数 %d'%number)
            
            images = []
            images = tdx.CaptureStocksDrawings(number, current)
            
            webchat.send_self("自选股监控")
            webchat.SendToGroup("自选股监控")
            i = 0
            for image in images:
                if ( i < number):
                    webchat.send_image_by_file_helper(stocks[i], image)
                    webchat.SendToGroup(stocks[i], image)
                i += 1
                time.sleep(0.5)
            time.sleep(50)

            tdx.UpdataRealTimeData()
            BeginSelectStockTask(tdx)       
            time.sleep(60)  
            tdx.SwitchToSelfChooseMainFrame()           
        else:
            print("time to sleep")
            time.sleep(2)
