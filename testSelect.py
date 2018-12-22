import win32gui
import win32con
import time
import win32api
import datetime
 
from tdx import condition
from tdx import loginWin

handle=loginWin.LoginWin().TdxLogin()
condition.SelectStocksWindow(handle).ExeSelectStocks(1)


 


