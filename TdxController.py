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
 
tmpStockWinPos = [-1, -4, -1, -4]

class tempStocks:
    def __init__(self):
        self.parent = win32gui.FindWindow('TdxW_MainFrame_Class','通达信金融终端V7.42 - [行情报价-临时条件股]')
        self.x = -1
        self.y = -4
        self.find = 0

    def GetTempSocktWindowPos(self):
        if (self.find == 0 and self.parent != 0):
            self.x, self.y, x1, y1 = win32gui.GetWindowRect(self.parent)
            self.find = 1
        return self.x, self.y
    
    def GetFirstStockPosition(self):
        pos = self.GetTempSocktWindowPos()
        x = pos[0] + 61
        y = pos[1] + 84
        print(x, y)
        return x, y

    def GetStockPosByIndex(self, index):
        diff = 20
        x, y = self.GetFirstStockPosition()
        if x != -1 and index > 0:
            y = y + index * diff
        return x, y

#必须先打开临时条件股
class TimeController:
    def __init__(self, x, y):
        self.parent = None
        self.left = x
        self.top = y

    def GetOneMinutePos(self):
        x = self.left + 51
        y = self.top + 35

        return x,y


    def GetMutiTimePos(self):
        x = self.left + 372
        y = self.top + 37

        return x,y


class ConditionSelectStocksWindow:
    def __init__(self):
        self.handle = win32gui.FindWindow('#32770','条件选股')

    def GetNumberSelected(self):
        handle = win32gui.FindWindowEx(self.handle, None, 'static', '选中数')
        numberHandle = win32gui.FindWindowEx(self.handle, handle, 'static', None)
        title = win32gui.GetWindowText(numberHandle)
        result = title.split('/', 1)
        return int(result[0])


#     #按索引选择公式
#     def Stock_option(self, index):
#         try:
#             gs = win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'ComboBox',None)
#             #time.sleep(1)
#             print(hex(gs))
#             win32gui.SendMessage(gs,win32con.CB_SHOWDROPDOWN,1,0)  #展开ComboBox列表框
#             time.sleep(1)
#             win32gui.SendMessage(gs,win32con.CB_SETCURSEL,index,0)#指向指定记录号
#             time.sleep(1)
#             win32gui.SendMessage(gs,win32con.WM_SETFOCUS,0,0)#选中按钮
#             time.sleep(1)
#             win32gui.SendMessage(gs,win32con.WM_KEYDOWN,0,0)#模拟按下指定键
#             win32gui.SendMessage(gs,win32con.WM_KEYUP,0,0) 
#             time.sleep(1)
#         except Exception as e:
#             print(sys._getframe().f_code.co_name+'\t'+str(e))


#    #按索引选择公式
#     def ImportCase(self):
#         try:
#             #tjxg = win32gui.FindWindow('#32770','条件选股')
#             yrfa = win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','引入方案')
#             win32gui.PostMessage(yrfa,win32con.BM_CLICK,0,0)
#             time.sleep(1)

#             fawj = win32gui.FindWindowEx(win32gui.FindWindow('#32770','选择选股方案文件'),None,'Button','确定')
#             win32gui.PostMessage(fawj,win32con.BM_CLICK,0,0)
#             time.sleep(1)
#         except Exception as e:
#             print(sys._getframe().f_code.co_name+'\t'+str(e))

#     #加入条件
#     def Join_condition(self):
#         try:
#             #time.sleep(5)
#             win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','加入条件'),win32con.BM_CLICK,0,0)
#             time.sleep(1)
#         except Exception as e:
#             print(sys._getframe().f_code.co_name+'\t'+str(e))

#     #执行选股
#     def begin_select_stocks(self):
#         try:
#             while win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Static','选股完毕. ') == 0:
#                 zs = win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','执行选股')
#                 print(zs)
#                 print(type(zs))
#                 win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','执行选股'),win32con.BM_CLICK,0,0)
#                 time.sleep(1)

#                 ensure_diagle=win32gui.FindWindowEx(win32gui.FindWindow('#32770','TdxW'),None,'Button','确定')
#                 if(ensure_diagle != 0):
#                     win32gui.PostMessage(ensure_diagle ,win32con.BM_CLICK,0,0)

#                 time.sleep(10)    

#                 print("执行选股")
#                 break
#         except Exception as e:
#             print(sys._getframe().f_code.co_name+'\t'+str(e))
        
#     #补数据
#     def Complement_data(self):
#         try:
#             time.sleep(1)
#             if win32gui.FindWindowEx(win32gui.FindWindow('#32770','TdxW'),None,'Button','是(&Y)') != 0:
#                 win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','TdxW'),None,'Button','是(&Y)'),win32con.BM_CLICK,0,0)
#                 time.sleep(5)
#                 print("补数据")
#         except Exception as e:
#             print(sys._getframe().f_code.co_name+'\t'+str(e))

#     #关闭选股器
#     def CloseSelectStockWindows(self):
#         time.sleep(5)
#         try:
#             while True:
#                 print("查看是否选股完成")
#                 time.sleep(1)
#                 if win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Static','选股完毕. ') != 0:
#                     win32gui.PostMessage(win32gui.FindWindow('#32770','条件选股'),win32con.WM_CLOSE,0,0)
#                     time.sleep(1)
#                     print("选股完毕")
#                     break
#         except Exception as e:
#             print(sys._getframe().f_code.co_name+'\t'+str(e))