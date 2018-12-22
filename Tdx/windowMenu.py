
import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
from tdx import stockListWin
from pc import Mouse

POS_DIFF={
    u'系统':[34,9],
    u'盘后数据下载':[87,248]
}

class Menus:
    def __init__(self, parent=stockListWin.StockListWin()):
        self.parent = parent

    def GetMenuPostion(self, str):
        p = self.parent.GetWindowPos()
        x = p[0] + POS_DIFF[str][0]
        y = p[1] + POS_DIFF[str][1]
        return x, y


    def OpenWindowByMenu(self, menu=u'系统', subMenu=u'盘后数据下载'):
        if self.parent != 0:
            Mouse.ClickPos(self.GetMenuPostion(menu), 0.5)
            Mouse.ClickPos(self.GetMenuPostion(subMenu), 0.5)
