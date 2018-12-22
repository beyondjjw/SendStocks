
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


class DownLoadDataAfterTradeWindow():
    def __init__(self, currentWin=u'行情报价-临时条件股'):
        self.curWin = currentWin
        self.x = 0
        self.y = 0
        self.handle=0

    def Open(self):
        curWindow = stockListWin.StockListWin(self.curWin)
        menu = windowMenu.Menus(curWindow)
        menu.OpenWindowByMenu(u'系统', u'盘后数据下载')
        self.handle = win32gui.FindWindow('#32770','盘后数据下载')
        if self.handle != 0:
            self.x, self.y, right, bottom=win32gui.GetWindowRect(win32gui.FindWindow('#32770','盘后数据下载'))
            print(self.x, self.y)

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

    def UpdataRealTimeData(self):
        try:
            self.Open()
            Mouse.ClickPos(self.GetControlPostion(u'日线和实时行情数据'), 1)
            Mouse.ClickPos(self.GetControlPostion(u'沪深分钟线'))
            Mouse.ClickPos(self.GetControlPostion(u'1分钟线数据'))
            Mouse.ClickPos(self.GetControlPostion(u'5分钟线数据'))
            Mouse.ClickButton(self.handle, u'开始下载')
            
            if self.IsOver(): 
                self.Close()
        
        except Exception as e:
            print(sys._getframe().f_code.co_name+'\t'+str(e))

    