
import win32gui
import win32api
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
import Capture
import WebChatMgr
import os
import threading

class TdxOperator():
    def __init__(self):
        self.webchat=WebChatMgr.WebChatManager()
        self.path =  'C:/new_tdx/'
        self.index = 87#系统选股公式一共90个
        self.webchat=WebChatMgr.WebChatManager()

    #打开通达信
    def Open_TDX(self):
        try:
            handle = win32process.CreateProcess(self.path+'TdxW.exe','',None,None,0,win32process.CREATE_NO_WINDOW,None, self.path,win32process.STARTUPINFO())#打开TB,获得其句柄
            time.sleep(3)
            TDX_handle = win32gui.FindWindow('#32770','通达信金融终端V7.42')

            time.sleep(3)

            #找免费行情
            Tab_handle = win32gui.FindWindowEx(win32gui.FindWindow('#32770','通达信金融终端V7.42'),None,'SysTabControl32','Tab1')
            p=win32gui.GetWindowRect(Tab_handle)
            #print(p)
            #print(p[2])
            #print(p[3])
            win32api.SetCursorPos([p[0]+170,p[1]+7])
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
            time.sleep(1)
            win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','通达信金融终端V7.42'),None,'Button','登录'),win32con.BM_CLICK,0,0)
            time.sleep(3)
            
            ads_handle = win32gui.FindWindow('#32770','通达信信息')
            print(ads_handle)
            win32gui.SendMessage(win32gui.FindWindow('#32770','通达信信息'),win32con.WM_CLOSE,0,0)
            
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))
        
    #登录信息框
    def CloseInfoTable(self):
        try:
            time.sleep(5)
            win32gui.PostMessage(win32gui.FindWindow('#32770','通达信信息'),win32con.WM_CLOSE,0,0)
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))


    #条件选股 Ctrl+T
    def Ctrl_T(self):
        try:
            win32api.keybd_event(17,0,0,0)#ctrl键位码是17
            win32api.keybd_event(84,0,0,0)#t键位码是84
            win32api.keybd_event(84,0,win32con.KEYEVENTF_KEYUP,0)#释放按键
            win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
            time.sleep(1)
            #win32gui.SendMessage(Tab_handle,0x130C,1,0)
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))

    #按索引选择公式
    def Stock_option(self, index):
        try:
            #tjxg = win32gui.FindWindow('#32770','条件选股')
            gs = win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'ComboBox',None)
            #time.sleep(1)
            print(hex(gs))
            win32gui.SendMessage(gs,win32con.CB_SHOWDROPDOWN,1,0)  #展开ComboBox列表框
            time.sleep(1)
            win32gui.SendMessage(gs,win32con.CB_SETCURSEL,index,0)#指向指定记录号
            time.sleep(1)
            win32gui.SendMessage(gs,win32con.WM_SETFOCUS,0,0)#选中按钮
            time.sleep(1)
            win32gui.SendMessage(gs,win32con.WM_KEYDOWN,0,0)#模拟按下指定键
            win32gui.SendMessage(gs,win32con.WM_KEYUP,0,0) 
            time.sleep(1)
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))


   #按索引选择公式
    def ImportCase(self):
        try:
            #tjxg = win32gui.FindWindow('#32770','条件选股')
            yrfa = win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','引入方案')
            win32gui.PostMessage(yrfa,win32con.BM_CLICK,0,0)
            time.sleep(1)

            fawj = win32gui.FindWindowEx(win32gui.FindWindow('#32770','选择选股方案文件'),None,'Button','确定')
            win32gui.PostMessage(fawj,win32con.BM_CLICK,0,0)
            time.sleep(1)
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))

    #加入条件
    def Join_condition(self):
        try:
            #time.sleep(5)
            win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','加入条件'),win32con.BM_CLICK,0,0)
            time.sleep(1)
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))

    #执行选股
    def begin_select_stocks(self):
        try:
            while win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Static','选股完毕. ') == 0:
                zs = win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','执行选股')
                print(zs)
                print(type(zs))
                win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Button','执行选股'),win32con.BM_CLICK,0,0)
                time.sleep(10)
                print("执行选股")
                break
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))
        
    #补数据
    def Complement_data(self):
        try:
            time.sleep(1)
            if win32gui.FindWindowEx(win32gui.FindWindow('#32770','TdxW'),None,'Button','是(&Y)') != 0:
                win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','TdxW'),None,'Button','是(&Y)'),win32con.BM_CLICK,0,0)
                time.sleep(5)
                print("补数据")
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))

    #关闭选股器
    def CloseSelectStockWindows(self):
        time.sleep(5)
        try:
            while True:
                print("查看是否选股完成")
                time.sleep(1)
                if win32gui.FindWindowEx(win32gui.FindWindow('#32770','条件选股'),None,'Static','选股完毕. ') != 0:
                    win32gui.PostMessage(win32gui.FindWindow('#32770','条件选股'),win32con.WM_CLOSE,0,0)
                    # time.sleep(1)
                    print("选股完毕")
                    break
        except Exception as e:
            self.webchat.warning(sys._getframe().f_code.co_name+'\t'+str(e))


    def KillSelf(self):
        try:
            print(os.popen('tasklist'))
            os.system('taskkill /IM TdxW.exe /F')
        except Exception as e:
            print("no Tdx: "+str(e))

    def GetReadyForSelect(self):
        self.KillSelf()
        self.Open_TDX()
        self.CloseInfoTable()
        
    
    def DoSelectStocksNow(self, index, imageName):
        self.Ctrl_T()
        self.Stock_option(index)
        self.Join_condition()
        self.begin_select_stocks()
        self.Complement_data()
        self.CloseSelectStockWindows()

    def DoImportSelectStockCase(self, index):
        self.Ctrl_T()
        self.ImportCase()
        self.begin_select_stocks()
        self.Complement_data()
        self.CloseSelectStockWindows()
        