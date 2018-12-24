

import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
from pc import KeyBoard
from pc import Mouse
from tdx import controlInMain

def get_child_windows(parent):        
    '''     
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''     
    if not parent:         
        return      
    hwndChildList = []     
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)          
    return hwndChildList 


class StockListWin():
    #行情报价-临时条件股
    #行情报价-自选股
    def __init__(self, str='行情报价-临时条件股'):
        self.classname = '通达信金融终端V7.42 - [%s]'%str
        self.handle = 0
        self.x = 0
        self.y = 0
        self.number = 0
        self.stockList = []

    def GetWindowPos(self):
        self.handle = win32gui.FindWindow('TdxW_MainFrame_Class', self.classname)
        if (self.Valid()):
            self.x, self.y, x1, y1 = win32gui.GetWindowRect(self.handle)
            # print(self.x, self.y, x1, y1)

        return self.x, self.y

    def Valid(self):
        return self.handle != 0

    def GetFirstStockPosition(self):
        if self.handle == 0:
            self.handle = win32gui.FindWindow('TdxW_MainFrame_Class', self.classname)
        pos = self.GetWindowPos()
        x = pos[0] + 61
        y = pos[1] + 84
        # print(x, y)
        return x, y

    def GetStockPosByIndex(self, index):
        if self.handle == 0:
            self.handle = win32gui.FindWindow('TdxW_MainFrame_Class', self.classname)
        diff = 20
        x, y = self.GetFirstStockPosition()
        if x != -1 and index > 0:
            y = y + index * diff
        return x, y

    def GetNumber(self):
        return self.number

    def Active(self):
        if self.handle == 0:
            self.handle = win32gui.FindWindow('TdxW_MainFrame_Class', self.classname)
        win32gui.SetForegroundWindow(self.handle)
        time.sleep(.1)

    def CountList(self):
        if self.handle == 0:
            self.handle = win32gui.FindWindow('TdxW_MainFrame_Class', self.classname)
        
        x, y = self.GetStockPosByIndex(0)
        Mouse.DoubleClick(x, y, 1)  
        controlInMain.CycleControl(self.x, self.y).ShowOneMinuteCycleDrawing()

        while True:
            h = win32gui.FindWindow('TdxW_MainFrame_Class', None)
            title = win32gui.GetWindowText(h)     
            result = title.replace(']','').split('-')
            if len(result) !=3 :
                break
            name=result[2]
            if self.stockList.count(name) == 0:
                self.stockList.append(name)
            elif self.stockList.count(name) == 1:
                break
            self.Active()
            KeyBoard.key_input_key('page_down')
            time.sleep(0.5)
        
        print(self.stockList)

        KeyBoard.key_input_key('page_down')

        return self.stockList