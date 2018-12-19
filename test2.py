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
# import WebChatMgr
import os
import threading
import TdxOperator

# webchat = WebChatMgr.WebChatManager()

def heart_beat(str):
    # chat = WebChatMgr.WebChatManager()
    # chat.send_heartbeat()
    print(str)
        
if __name__=='__main__':
    # t1 = t1 = threading.Thread(target=heart_beat,args=(u'heartbeat',))
    # t1.start()
    tdx = TdxOperator.TdxOperator()

    while 1:
        
        if int(time.strftime("%H%M%S")) >= 93000:
            
            tdx.OpenTdxForReady()
            index = 88
            indexName= "近期强势股,请看看低吸机会，找1分钟信号线是否变红，不要追高"
            imageName = "C:\\code\\pic\\qianshigu.jpg"
            tdx.DoSelectStocksNow(88, 6)
            tdx.DoSelectStocksNow(92, 1)
            Capture.WindowCapture(imageName)
            # webchat.SendImageToGroup(indexName, imageName)
            # webchat.send_image_by_file_helper(indexName, imageName)

            tdx.KillSelf()

            time.sleep(10*60)
        else:
            print("time to sleep")
            time.sleep(2)
            
 
