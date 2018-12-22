

import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui

class ShangZhengZhiShu():
    def __init__(self):
        self.handle = win32gui.FindWindow('TdxW_MainFrame_Class','通达信金融终端V7.42 - [分析图表-上证指数]')
        self.x = 0
        self.y = 0

    def GetWindowPos(self):
        if (self.handle != 0):
            self.x, self.y, x1, y1 = win32gui.GetWindowRect(self.handle)

        return self.x, self.y

     