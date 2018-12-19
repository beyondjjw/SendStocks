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

webchat = WebChatMgr.WebChatManager()

def ShowMultiTimeWindows(number):
    index = 0
    while index < number:
        tmpStock = TdxController.tempStocks()
        left, top = tmpStock.GetTempSocktWindowPos()

        # x, y = tmpStock.GetFirstStockPosition()
        # Mouse.DoubleClick(x, y)

        x, y = tmpStock.GetStockPosByIndex(index)
        Mouse.DoubleClick(x, y)    

        time.sleep(1)

        steps = 0
        timeCtller = TdxController.TimeController(left, top)
        x, y = timeCtller.GetOneMinutePos()
        Mouse.Click(x, y)
        steps += 1

        time.sleep(1)
        x, y = timeCtller.GetMutiTimePos()
        Mouse.Click(x, y)
        steps += 1

        time.sleep(2)

        imageName = "C:\\code\\pic\\tmp.jpg"
        Capture.window_capture(imageName)
        webchat.send_image_to_group("详细走势", imageName)
        
        
        while steps > 0:
            KeyBoardMgr.key_input_key('esc')
            steps -= 1
        
        index += 1



def heart_beat(str):
    chat = WebChatMgr.WebChatManager()
    chat.send_heartbeat()
    print(str)

def select_strong_gu_and_red_on_one_minute():
    tdx = TdxOperator.TdxOperator()
    tdx.OpenTdxForReady()
    msg = "近期强势，今天1分钟信号线已经变红，注意是否是1分钟一买位置附近刚变红"
    imageName = "C:\\code\\pic\\qianshigu.jpg"
    result = tdx.DoImportSelectStockCase(2)
    Capture.window_capture(imageName)
    webchat.send_image_to_group(msg, imageName)
    ShowMultiTimeWindows(result)
    # webchat.send_image_by_file_helper(msg, imageName)
    tdx.KillSelf()

def select_xiaoniaofei_gu_just_for_view():
    tdx = TdxOperator.TdxOperator()
    tdx.OpenTdxForReady()
    index = 87
    indexName= "每日小鸟飞选股,多看少动，一般对应30分钟3买，可能新风口启动"
    imageName = "C:\\code\\pic\\xiaoniaofei.jpg"
    result = tdx.DoSelectStocksNow(index, imageName)
    Capture.window_capture(imageName)
    webchat.send_image_to_group(indexName, imageName)
    webchat.send_image_by_file_helper(indexName, imageName)
    tdx.KillSelf()

        
if __name__=='__main__':
    t1 = t1 = threading.Thread(target=heart_beat,args=(u'heartbeat',))
    t1.start()

    while 1:
        
        if int(time.strftime("%H%M%S")) >= 93000 :
            # select_xiaoniaofei_gu_just_for_view()
            # time.sleep(5 * 60)
            select_strong_gu_and_red_on_one_minute()
            time.sleep(1)

            time.sleep(5 * 60)

            tdx = TdxOperator.TdxOperator()
            tdx.DoUpdateRetimeData()

            

        # elif int(time.strftime("%H%M%S")) > 130000:
            # select_strong_gu_and_red_on_one_minute()
            # time.sleep(5 * 60)

        else:
            print("time to sleep")
            time.sleep(2)
            
 
