import win32gui
import win32con
import time
import win32api
import datetime
from pc import Mouse
from pc import KeyBoard
 
# from tdx import condition
# from tdx import loginWin

# handle=loginWin.LoginWin().TdxLogin()
# condition.SelectStocksWindow(handle).ExeSelectStocks(1)


    
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

names = []

while True:
    pacthHandle = win32gui.FindWindow('TdxW_MainFrame_Class', None)
    if pacthHandle == 0:
        break
    title = win32gui.GetWindowText(pacthHandle)     
    result = title.replace(']','').split('-')
    name=result[2]
    if names.count(name) == 0:
        names.append(name)
    elif names.count(name) == 1:
        break
    print(names)

    win32gui.SetForegroundWindow(pacthHandle)
    time.sleep(.1)
    KeyBoard.key_input_key('page_down')
    time.sleep(.1)

print(names)


# pacthHandle = win32gui.FindWindow('TdxW_MainFrame_Class', None)
# win32gui.SetForegroundWindow(pacthHandle)
# print('pacthhandle %d'%pacthHandle)
# title = win32gui.GetWindowText(pacthHandle)     
# clsname = win32gui.GetClassName(pacthHandle)
# print(clsname, title)

# childs = []
# childs = get_child_windows(pacthHandle)
# for h in childs:
#     title = win32gui.GetWindowText(h)     
#     clsname = win32gui.GetClassName(h)
#     print(clsname, title)
 


