
from pc import Mouse
from pc import KeyBoard
import time

#必须先打开临时条件股
class CycleControl:
    def __init__(self, x, y):
        self.left = x
        self.top = y

    def GetOneMinutePos(self):
        x = self.left + 51
        y = self.top + 35
        return x,y


    def GetMutiTimePos(self):
        x = self.left + 372
        y = self.top + 37
        return x,y
    
    def ScaleDrawing(self, dir='small', times = 3):
        Mouse.Click(1200, 200, 1)
        for i in range(0,times):
            if dir == 'small':
                KeyBoard.key_input_key('down_arrow')
            else: 
                KeyBoard.key_input_key('up_arrow')
            i += 1

    def ShowOneMinuteCycleDrawing(self):
        Mouse.ClickPos(self.GetOneMinutePos(), 1)

    def ShowMultiCycle(self):
        Mouse.ClickPos(self.GetOneMinutePos())
        Mouse.ClickPos(self.GetMutiTimePos())
        self.ScaleDrawing()
        time.sleep(3)

    def QuitMultiCycle(self):
        KeyBoard.key_input_key('esc')
        KeyBoard.key_input_key('esc')

class SelfChoose:
    def __init__(self, x, y):
        self.parentPos = [x, y]
        self.diff = [554, 865]

    def GetSelfChooseButtonPos(self):
        return self.parentPos[0] + self.diff[0], self.parentPos[1] + self.diff[1]

   
