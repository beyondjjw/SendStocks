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



class SelectStockCaseFileWindow:
    def __init__(self):
        self.handle = win32gui.FindWindow('#32770','选择选股方案文件')

    def GetCasePostionByIndex(self, index):
        time.sleep(0.5)
        pos = win32gui.GetWindowRect(self.handle)
        return pos[0] + 5, pos[1] + 20 + index * 15

    def SelectCaseByIndex(self, index):
        x, y = self.GetCasePostionByIndex(index)
        Mouse.DoubleClick(x, y, 0.05) 

class SelectStocksWindow:
    def __init__(self):
        KeyBoard.inputCompositeKeys(['ctrl', 't'])
        self.handle = win32gui.FindWindow('#32770','条件选股')
        self.over = False

    #是否选股完成
    def IsOver(self):
        if(self.handle == 0): 
            return True
        while self.over != True:
            time.sleep(1)
            if win32gui.FindWindowEx(self.handle,None,'Static','选股完毕. ') != 0:
                self.over = True
        return self.over            

    def GetNumberSelected(self):
        result = '0/0'
        if(self.IsOver()):
            handle = win32gui.FindWindowEx(self.handle, None, 'static', '选中数')
            numberHandle = win32gui.FindWindowEx(self.handle, handle, 'static', None)
            title = win32gui.GetWindowText(numberHandle)
            result = title.split('/', 1)
        return int(result[0])

     #按索引选择方案
    def ImportCase(self, index):
        if self.handle == 0:
            return
        Mouse.ClickButton(self.handle, '引入方案')
        SelectStockCaseFileWindow().SelectCaseByIndex(index)

    #执行选股
    def Do(self):
        if(self.handle == 0): 
            return
        Mouse.ClickButton(self.handle, '执行选股')
        EnsureWinowJump = win32gui.FindWindow('#32770','TdxW')
        if(EnsureWinowJump != 0):
            Mouse.ClickButton(EnsureWinowJump, '确定')
        time.sleep(3)    

    #关闭选股器
    def CloseWindow(self):   
        result = 0
        if(self.IsOver()):
            result = self.GetNumberSelected()
            Mouse.ClickController(self.handle)
        return result
                
    def ExeSelectStocks(self, index):
        result = 0
        self.ImportCase(index)
        self.Do()
        if(self.IsOver()):
            result = self.CloseWindow()
        return result



