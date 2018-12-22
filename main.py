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
        time.sleep(30)
        chat.send_heartbeat()
        if int(time.strftime("%H%M%S")) >= 150100 :
            pcMgr.ShutDown(2)
            

def StartTasks():
    t1 = threading.Thread(target=heart_beat,args=(u'heartbeat',))
    t1.start()

def SendStocksInfo(msg, images):
    for image in images:
        webchat.SendToGroup(msg, image)
        
if __name__=='__main__':
    
    StartTasks()
    time.sleep(10)
    
    while 1:
        
        if int(time.strftime("%H%M%S")) >= 93000 :
            tdx = tdxOperator.TdxOperator()
            tdx.OpenTdx()
            
            tdx.UpdataRealTimeData()
            time.sleep(1)

            caseIndex = 1
            result = tdx.DoSelectStocksNow(caseIndex)
            stocksWin = stockListWin.StockListWin()
            images = []
            images = tdx.CaptureStocksDrawings(result, stocksWin)
            SendStocksInfo(CaseInfo[caseIndex], images)
            if(result < 5):
                tdx.DoSelectStocksNow(2)

            time.sleep(5*60)

        else:
            print("time to sleep")
            time.sleep(2)
            
 
