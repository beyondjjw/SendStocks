
import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
from tdx import windowMenu
from tdx import stockListWin
from pc import Mouse


DIFF={
    u'日线数据':[(250-216),(205-168)],    
    u'日线和实时行情数据':[(240-216),(262-168)],
    u'沪深分钟线':[(320-216),(210-168)],  
    u'1分钟线数据':[(240-216),(240-168)],     
    u'5分钟线数据':[(240-216), (263-168)],     
}


class DownLoadDataAfterTradeWindow:
    def __init__(self, parent):
        self.x = 0
        self.y = 0
        self.handle=0
        self.parent = parent

    def Open(self):
        win32gui.SetForegroundWindow(self.parent)
        pos = win32gui.GetWindowRect(self.parent)
        menu = windowMenu.Menus(pos[0], pos[1])
        menu.OpenWindowByMenu(u'系统', u'盘后数据下载')
        self.handle = win32gui.FindWindow('#32770','盘后数据下载')
        if self.handle != 0:
            self.x, self.y, right, bottom=win32gui.GetWindowRect(win32gui.FindWindow('#32770','盘后数据下载'))
            # print(self.x, self.y)

    def GetControlPostion(self, name):
        return self.x + DIFF[name][0], self.y + DIFF[name][1]

    def IsOver(self):
        while True:
            time.sleep(2)
            if win32gui.FindWindowEx(self.handle, None,'Static','下载完毕.') != 0:
                break
        return True

    def Close(self):
        time.sleep(0.05)
        win32gui.PostMessage(self.handle, win32con.WM_CLOSE, 0, 0)
        time.sleep(0.05)

    # 0x1，下1分钟数据线，0x2:下5分钟线, 0x3,1分钟和5分钟都下，0x4下日线，0x7：日线，1分钟，5分钟全下
    def UpdataRealTimeData(self, dataType=1):
        try:
            self.Open()

            if dataType & int('0x1', 16):
                Mouse.ClickPos(self.GetControlPostion(u'沪深分钟线'))
                Mouse.ClickPos(self.GetControlPostion(u'1分钟线数据'))
            
            if dataType & int('0x2', 16):
                Mouse.ClickPos(self.GetControlPostion(u'沪深分钟线'))
                Mouse.ClickPos(self.GetControlPostion(u'5分钟线数据'))

            if dataType & int('0x4', 16):
                Mouse.ClickPos(self.GetControlPostion(u'日线数据'))
                Mouse.ClickPos(self.GetControlPostion(u'日线和实时行情数据'))

            Mouse.ClickButton(self.handle, u'开始下载')
            
            if self.IsOver(): 
                self.Close()
        
        except Exception as e:
            print(sys._getframe().f_code.co_name+'\t'+str(e))

    