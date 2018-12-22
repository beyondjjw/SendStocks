

import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui

class StockListWin():
    #行情报价-临时条件股
    #行情报价-自选股
    def __init__(self, number=0, str='行情报价-临时条件股'):
        self.classname = '通达信金融终端V7.42 - [%s]'%str
        self.handle = win32gui.FindWindow('TdxW_MainFrame_Class', self.classname)
        self.x = 0
        self.y = 0
        self.number = 0

    def GetWindowPos(self):
        if (self.Valid()):
            self.x, self.y, x1, y1 = win32gui.GetWindowRect(self.handle)

        return self.x, self.y

    def Valid(self):
        return self.handle != 0

    def GetFirstStockPosition(self):
        pos = self.GetWindowPos()
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

    def GetNumber(self):
        return self.number

     