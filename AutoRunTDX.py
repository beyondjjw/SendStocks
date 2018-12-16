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

webchat = WebChatMgr.WebChatManager()

def heart_beat(str):
    chat = WebChatMgr.WebChatManager()
    chat.send_heartbeat()
    print(str)

def select_strong_gu_and_red_on_one_minute():
    tdx = TdxOperator.TdxOperator()
    tdx.GetReadyForSelect()
    msg = "近期强势，今天1分钟信号线已经变红，注意是否是1分钟一买位置附近刚变红"
    imageName = "C:\\code\\pic\\qianshigu.jpg"
    tdx.DoImportSelectStockCase(1)
    Capture.window_capture(imageName)
    webchat.send_image_to_group(msg, imageName)
    webchat.send_image_by_file_helper(msg, imageName)
    tdx.KillSelf()

def select_xiaoniaofei_gu_just_for_view():
    tdx = TdxOperator.TdxOperator()
    tdx.GetReadyForSelect()
    index = 87
    indexName= "每日小鸟飞选股,多看少动，一般有新的风口启动"
    imageName = "C:\\code\\pic\\xiaoniaofei.jpg"
    tdx.DoSelectStocksNow(index, imageName)
    Capture.window_capture(imageName)
    webchat.send_image_to_group(indexName, imageName)
    webchat.send_image_by_file_helper(indexName, imageName)
    tdx.KillSelf()

        
if __name__=='__main__':
    t1 = t1 = threading.Thread(target=heart_beat,args=(u'heartbeat',))
    t1.start()
    tdx = TdxOperator.TdxOperator()

    while 1:
        
        if int(time.strftime("%H%M%S")) >= 93000 and int(time.strftime("%H%M%S")) <= 113000:
            select_xiaoniaofei_gu_just_for_view()
            time.sleep(10 * 60)

        elif int(time.strftime("%H%M%S")) > 113000:
            select_strong_gu_and_red_on_one_minute()
            time.sleep(5 * 60)

        else:
            print("time to sleep")
            time.sleep(2)
            
 
