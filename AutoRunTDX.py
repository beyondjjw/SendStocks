# -*- coding: UTF-8 -*-

import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
import Capture
import WebChatMgr
import os
import threading
import TdxOperator

import TdxController
import Mouse
import KeyBoardMgr
import Seconds
import StockCase



webchat = WebChatMgr.WebChatManager()

def ShowMultiTimeWindows(number):
    if number == 0: 
        return

    tmpStock = TdxController.tempStocks()
    left, top = tmpStock.GetTempSocktWindowPos()

    x, y = tmpStock.GetStockPosByIndex(0)
    Mouse.DoubleClick(x, y, Seconds.stop(1))    

    timeCtller = TdxController.TimeController(left, top)
    x, y = timeCtller.GetOneMinutePos()
    Mouse.Click(x, y, Seconds.stop(1))
    x, y = timeCtller.GetMutiTimePos()
    Mouse.Click(x, y, Seconds.stop(3))
   
    # 缩小图
    Mouse.Click(1200, 200, Seconds.stop(1))
    KeyBoardMgr.key_input_key('down_arrow')
    KeyBoardMgr.key_input_key('down_arrow')
    KeyBoardMgr.key_input_key('down_arrow', Seconds.stop(2))

    imageName = "C:\\code\\pic\\tmp.jpg"
    Capture.WindowCapture(imageName)
    webchat.SendToGroup("1分钟，5分钟，30分钟详细走势", imageName)

    index = 1
    while index < number:
        KeyBoardMgr.key_input_key('page_down', Seconds.stop(3))
        Capture.WindowCapture(imageName)
        webchat.SendToGroup("1分钟，5分钟，30分钟详细走势", imageName)
        # webchat.send_image_by_file_helper("1分钟，5分钟，30分钟详细走势", imageName)
        index += 1

    KeyBoardMgr.key_input_key('esc')
    KeyBoardMgr.key_input_key('esc')



def heart_beat(str):
    chat = WebChatMgr.WebChatManager()
    chat.send_heartbeat()
    print(str)

def SelectStocksByCase(index):
    tdx = TdxOperator.TdxOperator()
    tdx.OpenTdxForReady()
    msg = StockCase.GetCaseName(index)
    imageName = StockCase.GetCaseResultImagePath(index)
    print(msg, imageName)
    result = tdx.DoSelectStockByImportCase(index)
    Capture.WindowCapture(imageName)
    webchat.SendToGroup(msg, imageName)
    # webchat.send_image_by_file_helper(msg, imageName)
    ShowMultiTimeWindows(result)
    tdx.KillSelf()
    return result

# def select_xiaoniaofei_gu_just_for_view():
#     tdx = TdxOperator.TdxOperator()
#     tdx.OpenTdxForReady()
#     index = 87
#     indexName= "每日小鸟飞选股,多看少动，一般对应30分钟3买，可能新风口启动"
#     imageName = "C:\\code\\pic\\xiaoniaofei.jpg"
#     result = tdx.DoSelectStocksNow(index, imageName)
#     Capture.WindowCapture(imageName)
#     # webchat.SendToGroup(indexName, imageName)
#     webchat.send_image_by_file_helper(indexName, imageName)
#     tdx.KillSelf()

        
if __name__=='__main__':
    t1 = t1 = threading.Thread(target=heart_beat,args=(u'heartbeat',))
    t1.start()

    time.sleep(10)
    webchat.SendToGroup("开始自动化选股流程，OK, I'm ready", '')

    while 1:
        
        if int(time.strftime("%H%M%S")) >= 93000 :
            tdx = TdxOperator.TdxOperator()
            tdx.DoUpdateRetimeData()
            time.sleep(1)

            result = SelectStocksByCase(1)
            result = 0
            if(result < 5):
                SelectStocksByCase(2)

            time.sleep(5 * 60)

        else:
            print("time to sleep")
            time.sleep(2)
            
 
