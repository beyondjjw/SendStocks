import win32gui
import win32api
import win32com
from win32.lib import win32con
import time
import win32process
import datetime
import win32ui
import sys
import os

def ShutDown(timeout):
    cancle = "shutdown -a"
    os.system(cancle)

    cmd = "shutdown -s -t %(timeout)d -f"%{'timeout':timeout}
    os.system(cmd)
    time.sleep(10)

def CheckProcessExist(process_name):
    if process_name in os.popen('tasklist /FI "IMAGENAME eq %s"'%process_name).read():
        return True
    return False