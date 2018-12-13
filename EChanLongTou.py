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
import os
import threading
import win32clipboard as w
import WebChatMgr


def timeSelectStock():
    try:
        time.sleep(1)
        yi = win32gui.FindWindow('Afx:00400000:8:00010003:00000000:01AF057F', ' - [易缠客户端-上海禅定信息技术有限公司:]')
        print(yi)
        
        yichan = win32gui.FindWindowEx(win32gui.FindWindow('Afx:00400000:8:00010003:00000000:01AF057F', ' - [易缠客户端-上海禅定信息技术有限公司:]'),None,'Button','时间选股')
        print("yichan ")
        print(yichan)

    except Exception as e:
        webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))


def CopyStocks():
    try:
        time.sleep(5)
        zs = win32gui.FindWindowEx(win32gui.FindWindow('#32770','易缠'),None,'Button','复制股票代码到剪切板')
        print("copy to clip")
        print(zs)
        print(type(zs))
        win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','执行选股'),win32con.BM_CLICK,0,0)
    except Exception as e:
        webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))

def CloseTiShi():
    try:
        time.sleep(2)
        zs = win32gui.PostMessage(win32gui.FindWindow('#32770','提示'),win32con.WM_CLOSE,0,0)
        print("CloseTiShi")
        print(zs)
        print(type(zs))
    except Exception as e:
        webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))



def getText():#读取剪切板  
    print("getText")
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_TEXT)  
    w.CloseClipboard()  
    print(d)
    return d    
        
def send_long_tou():
    timeSelectStock()
    CopyStocks()
    CloseTiShi()
    str = getText()
    # chat = WebChatMgr.WebChatManager()
    # chat.send_longtou_self(str.decode("utf-8"))

send_long_tou()