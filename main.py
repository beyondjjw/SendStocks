# -*- coding: UTF-8 -*-

import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
from winsofts import webChatMgr
from pc import pcMgr
import threading
from tdx import tdxOperator
from tdx import stockListWin


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

def BeginSelectStockTask(tdx):
    caseIndex = 1
    result = 0
    while result <= 3 and caseIndex <= 2:
        result = tdx.DoSelectStocksNow(caseIndex)
        stocksWin = stockListWin.StockListWin()
        if result > 0:
            tdx.AddTempStocksToSelfChoose(result)
        images = []
        images = tdx.CaptureStocksDrawings(result, stocksWin)
        SendStocksInfo(CaseInfo[caseIndex], images)
        if result <= 3:
            caseIndex = 2
        else:
            break
        tdx.SwitchToSelfChooseMainFrame()
        
if __name__=='__main__':
    
    StartTasks()
    time.sleep(10)
    
    while 1:
        
        if int(time.strftime("%H%M%S")) >= 92900 :
            tdx = tdxOperator.TdxOperator()
            tdx.OpenTdx()
            
            tdx.SwitchToSelfChooseMainFrame()
            tdx.SyncSelfChoose()

            current = stockListWin.StockListWin(u'行情报价-自选股')
            stocks = current.CountList()
            number = len(stocks)
            print(u'自选股数%d'%number)
            
            images = []
            images = tdx.CaptureStocksDrawings(number, current)
            
            # webchat.send_self("自选股监控")
            webchat.SendToGroup("自选股监控")
            i = 0
            for image in images:
                # webchat.send_image_by_file_helper(stocks[i], image)
                webchat.SendToGroup(stocks[i], image)
                i += 1
                time.sleep(2)
            # time.sleep(50)

            tdx.UpdataRealTimeData()
            BeginSelectStockTask(tdx)       
            # time.sleep(60)             
        else:
            print("time to sleep")
            time.sleep(2)
            
 
