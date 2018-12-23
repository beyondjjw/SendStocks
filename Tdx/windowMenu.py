
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
    u'盘后数据下载':[87,248],
    u'同步':[18,57],
    u'上传自选股':[20,77]
}

class Menus:
    def __init__(self, x, y):
        self.parent_pos = [x,y]

    def GetMenuPostion(self, str):
        x = self.parent_pos[0] + POS_DIFF[str][0]
        y = self.parent_pos[1] + POS_DIFF[str][1]
        return x, y

    def OpenWindowByMenu(self, menu=u'系统', subMenu=u'盘后数据下载'):
        Mouse.ClickPos(self.GetMenuPostion(menu), 0.5)
        Mouse.ClickPos(self.GetMenuPostion(subMenu), 0.5)

