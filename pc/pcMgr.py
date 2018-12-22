import os
import time

def ShutDown(timeout):
    cancle = "shutdown -a"
    os.system(cancle)

    cmd = "shutdown -s -t %(timeout)d -f"%{'timeout':timeout}
    os.system(cmd)
    time.sleep(10)
