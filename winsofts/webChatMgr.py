from wxpy import *
import time
import threading

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton()
        return Singleton._instance


class WebChatManager(Singleton):
    def __init__(self):
        self.bot = Bot(True, False)
     
    def SendToGroup(self, msg, filepath='', groupName='欢乐股'):
        find = False
        groups = self.bot.groups()
        for group in groups:
            print(group)
            
        # if not find :
        #     self.send_self('发送消息给群%s失败，请给群发消息激活'%groupName)
        #     return
            
        group = self.bot.groups().search(groupName)[0]
        group.send(msg)
        if(filepath != ''):
            group.send_image(filepath)
    
    def send_image_by_file_helper(self, msg, filepath):
        self.bot.file_helper.send(msg)
        self.bot.file_helper.send_image(filepath)

    def send_self(self, msg):
        self.bot.file_helper.send(time.strftime("%H:%M:%S") + msg)

    def send_heartbeat(self):
        self.bot.file_helper.send("开始自动化选股流程，OK, I'm ready", '')
        while 1:
            time.sleep(30)
            try:
                self.bot.file_helper.send("heartbeat "+ time.strftime("%H:%M:%S"))
            except Exception as e:
                print("心跳发送失败" + time.strftime("%H:%M:%S") + str(e))

    def warning(self, warnings):
        self.bot.file_helper.send(time.strftime("%H:%M:%S") + warnings)



   