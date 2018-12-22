import win32gui
import win32con
import time
import win32api
import datetime
 
from tdx import ConditionSelectStock
from tdx import LoginWin

LoginWin.LoginWin().TdxLogin()
ConditionSelectStock.SelectStocksWindow().ExeSelectStocks(1)


 


