
import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
import os
import threading
from tdx import condition
from tdx import loginWin
from pc import KeyBoard
from tdx import windowMenu
from tdx import stockListWin
from tdx import downloadDataWin
from pc import Mouse
from tdx import controlInMain
from winsofts import capture
from tdx import addToSelfChoose


    
def find_idxSubHandle(pHandle, winClass, index=0):
    """
    已知子窗口的窗体类名
    寻找第index号个同类型的兄弟窗口
    """
    assert type(index) == int and index >= 0
    handle = win32gui.FindWindowEx(pHandle, 0, winClass, None)
    while index > 0:
        handle = win32gui.FindWindowEx(pHandle, handle, winClass, None)
        print(hex(handle))
        index -= 1
    return handle

def find_subHandle(pHandle, winClassList):
    """
    递归寻找子窗口的句柄
    pHandle是祖父窗口的句柄
    winClassList是各个子窗口的class列表，父辈的list-index小于子辈
    """
    assert type(winClassList) == list
    if len(winClassList) == 1:
        return find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
    else:
        pHandle = find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
        return find_subHandle(pHandle, winClassList[1:])

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

class TdxOperator():
    def __init__(self):
        self.imagePath='C:\\pic\\'
        self.handle = 0
        self.pos = []
    
    def OpenTdx(self):
        self.handle = loginWin.LoginWin().TdxLogin()
        if (self.handle is not None):
            self.pos = win32gui.GetWindowRect(self.handle)
        else:
            self.pos = [-1,-4]

    def UpdataRealTimeData(self):
        downloadDataWin.DownLoadDataAfterTradeWindow(self.handle).UpdataRealTimeData()
        
    def KillSelf(self):
        try:
            print(os.popen('tasklist'))
            os.system('taskkill /IM TdxW.exe /F')
        except Exception as e:
            print("no Tdx: "+str(e))
    
    def DoSelectStocksNow(self, index=1):
        return condition.SelectStocksWindow(self.handle).ExeSelectStocks(index)

    def CaptureStocksDrawings(self, number=0, stocksWin=stockListWin.StockListWin()):
        pictures = []

        if number <= 0:
            return pictures

        left, top = stocksWin.GetWindowPos()
        tc = controlInMain.CycleControl(left, top)

        for index in range(0, number):
            x, y = stocksWin.GetStockPosByIndex(index)
            if ( index == 0):
                Mouse.DoubleClick(x, y, 1)  
                tc.ShowMultiCycle()
            else:
                center = [int(self.pos[2]/3), int(self.pos[3]/3)]
                print(center)
                Mouse.ClickPos(center)
                KeyBoard.key_input_key('page_down', 2)

            imageName = self.imagePath + "%d.jpg"%index
            capture.WindowCapture(imageName)
            pictures.append(imageName)
            index += 1

        tc.QuitMultiCycle()
        return pictures

    def AddTempStocksToSelfChoose(self, number):
        addToSelfChoose.PatchOperatorWindow(self.handle, number).AddAllToSelfChoose()

    def SwitchToSelfChooseMainFrame(self):
        Mouse.ClickPos(controlInMain.SelfChoose(self.pos[0], self.pos[1]).GetSelfChooseButtonPos())

    def SyncSelfChoose(self):
        windowMenu.Menus(self.pos[0], self.pos[1]).OpenWindowByMenu(u'同步', u'上传自选股')
        time.sleep(1)
        h = win32gui.FindWindow('#32770', u'执行进度')
        Mouse.ClickButton(h, u'完成')

    def GetCurrentWindowHandle(self):
        return self.handle












