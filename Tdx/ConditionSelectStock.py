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
import Mouse

class SelectStockCaseFileWindow:
    def __init__(self):
        self.handle = win32gui.FindWindow('#32770','选择选股方案文件')
    
    def GetCasePostionByIndex(self, index):
        pos = win32gui.GetWindowRect(self.handle)
        return pos[0] + 5, pos[1] + 20 + index * 15

    def SelectCaseByIndex(self, index):
        x, y = self.GetCasePostionByIndex(index)
        Mouse.DoubleClick(x, y)
        time.sleep(0.05)
 

class SelectStocksWindow:
    def __init__(self):
        self.handle = win32gui.FindWindow('#32770','条件选股')

    #是否选股完成
    def IsOver(self):
        if(self.handle == 0): 
            return False
        while True:
            time.sleep(1)
            if win32gui.FindWindowEx(self.handle,None,'Static','选股完毕. ') != 0:
                return True 
        return False            

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
        yrfa = win32gui.FindWindowEx(self.handle, None,'Button','引入方案')
        win32gui.PostMessage(yrfa, win32con.BM_CLICK,0,0)
        time.sleep(0.5)
        case = SelectStockCaseFileWindow()
        case.SelectCaseByIndex(index)
        time.sleep(0.5)

    #执行选股
    def begin_select_stocks(self):
        if(self.handle == 0): 
            return
        
        while win32gui.FindWindowEx(self.handle,None,'Static','选股完毕. ') == 0:
            zs = win32gui.FindWindowEx(self.handle,None,'Button','执行选股')
            print(zs)
            print(type(zs))
            win32gui.PostMessage(win32gui.FindWindowEx(self.handle,None,'Button','执行选股'),win32con.BM_CLICK,0,0)
            time.sleep(1)

            EnsureWinowJump = win32gui.FindWindow('#32770','TdxW')
            if(EnsureWinowJump != 0):
                win32gui.PostMessage(win32gui.FindWindowEx(EnsureWinowJump, None,'Button','确定') ,win32con.BM_CLICK,0,0)
            print("执行选股")
            time.sleep(5)    
            break

    #关闭选股器
    def CloseWindow(self):   
        result = 0
        if(self.IsOver()):
            print("选股完毕")
            result = self.GetNumberSelected()
            win32gui.PostMessage(self.handle, win32con.WM_CLOSE,0,0)
        return result
                
        


    # #按索引选择选股公式
    # def Stock_option(self, index):
    #     if(self.handle):
    #         gs = win32gui.FindWindowEx(self.handle,None,'ComboBox',None)
    #         win32gui.SendMessage(gs,win32con.CB_SHOWDROPDOWN,1,0)  #展开ComboBox列表框
    #         time.sleep(0.5)
    #         win32gui.SendMessage(gs,win32con.CB_SETCURSEL,index,0)#指向指定记录号
    #         time.sleep(0.5)
    #         win32gui.SendMessage(gs,win32con.WM_SETFOCUS,0,0)#选中按钮
    #         time.sleep(0.5)
    #         Mouse.ClickController(gs)
    #         time.sleep(0.5)

    # #加入条件
    # def Join_condition(self):
    #     try:
    #         #time.sleep(5)
    #         win32gui.PostMessage(win32gui.FindWindowEx(self.handle,None,'Button','加入条件'),win32con.BM_CLICK,0,0)
    #         time.sleep(1)
    #     except Exception as e:
    #         print(sys._getframe().f_code.co_name+'\t'+str(e))

    
        
    # #补数据
    # def Complement_data(self):
    #     try:
    #         time.sleep(1)
    #         if win32gui.FindWindowEx(win32gui.FindWindow('#32770','TdxW'),None,'Button','是(&Y)') != 0:
    #             win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','TdxW'),None,'Button','是(&Y)'),win32con.BM_CLICK,0,0)
    #             time.sleep(5)
    #             print("补数据")
    #     except Exception as e:
    #         print(sys._getframe().f_code.co_name+'\t'+str(e))

    