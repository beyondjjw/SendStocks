# -*- coding: UTF-8 -*-

# 该文件描述通达信的控件信息，比如控件类，控件名称，控件相对父控件的位置

import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
from pc import Mouse
from pc import KeyBoard

class AddToSelfChoose:
    def __init__(self):
        self.handle = self.handle = win32gui.FindWindow('#32770',u'加入到自选股/板块')

    def OK(self):
        time.sleep(1)
        Mouse.ClickButton(self.handle, u'确定')


class PatchOperatorWindow:
    def __init__(self, parent, number):
        win32gui.SetForegroundWindow(parent)
        KeyBoard.inputCompositeKeys(['ctrl', 'a'])
        titleName=u'批量操作本屏品种[%d只] '%number
        self.handle = win32gui.FindWindow('#32770',titleName)
     
    def AddAllToSelfChoose(self):
        time.sleep(1)
        Mouse.ClickButton(self.handle, u'全选中')
        Mouse.ClickButton(self.handle, u'加入到板块')
        AddToSelfChoose().OK()

    

    



