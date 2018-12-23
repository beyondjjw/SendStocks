
import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
import os
from pc import Mouse

def CheckProcessExist(process_name):
    if process_name in os.popen('tasklist /FI "IMAGENAME eq %s"'%process_name).read():
        return True
    return False

class LoginWin:
    def __init__(self):
        self.handle = None
        self.path =  'C:/new_tdx/'
    
    def KillSelf(self):
        try:
            print(os.popen('tasklist'))
            os.system('taskkill /IM TdxW.exe /F')
        except Exception as e:
            print("no Tdx: "+str(e))

    #通达信登陆
    def TdxLogin(self):
        try:
            self.KillSelf()
            # find = CheckProcessExist('TdxW.exe')
            
            win32process.CreateProcess(self.path+'TdxW.exe','',None,None,0,win32process.CREATE_NO_WINDOW,None, self.path,win32process.STARTUPINFO())#打开TB,获得其句柄
            time.sleep(3)
            self.handle = win32gui.FindWindow('#32770','通达信金融终端V7.42')
            #找免费行情
            Tab_handle = win32gui.FindWindowEx(self.handle,None,'SysTabControl32','Tab1')
            p=win32gui.GetWindowRect(Tab_handle)
            Mouse.Click(p[0]+170, p[1]+7, 1)

            login = win32gui.FindWindowEx(self.handle,None,'Button','登录')
            if login != 0:
                win32gui.PostMessage(win32gui.FindWindowEx(self.handle,None,'Button','登录'),win32con.BM_CLICK,0,0)
            time.sleep(10)
            EnsureWinowJump = win32gui.FindWindow('#32770','TdxW')
            if(EnsureWinowJump != 0):
                Mouse.ClickButton(EnsureWinowJump, '确定')
                time.sleep(10)
            self.CloseInfoTable()  

            h = win32gui.FindWindow('TdxW_MainFrame_Class', None)
            win32gui.SetForegroundWindow(h)
            return h
            
        except Exception as e:
            print(sys._getframe().f_code.co_name+'\t'+str(e))

    #登录信息框
    def CloseInfoTable(self):
        info = win32gui.FindWindow('#32770','通达信信息')
        if info != 0:
            win32gui.PostMessage(info,win32con.WM_CLOSE,0,0)
        time.sleep(2)
       

