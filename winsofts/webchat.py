#-*-coding:utf8-*-
import itchat
import datetime, os, platform,time

def login():
    itchat.auto_login(hotReload=True)  # 首次扫描登录后后续自动登录

def send_msg_to_friend(msg, name='炒股小号'):
    users = itchat.search_friends(name='炒股小号')   # 使用备注名来查找实际用户名
    #获取好友全部信息,返回一个列表,列表内是一个字典
    print(users)
    #获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    itchat.send(msg, toUserName = userName)
    print('succeed')

def send_to_group(msg, imagepath='', name='欢乐股A'):
    group  = itchat.get_chatrooms(update=True)
    for g in group:
        if g['NickName'] == name:
            to_group = g['UserName']
            if msg != '':
                itchat.send(msg, to_group)
            # time.sleep(.5)
            if imagepath != '':
                # itchat.send_image(imagepath, to_group)
                itchat.send_file(imagepath, to_group)
            break

def send_to_my_file_helper(msg, imagepath=''):
    itchat.send(msg, 'filehelper')
    if imagepath != '':
        # time.sleep(.5)
        itchat.send_image(imagepath, 'filehelper')

def send(msg, imagepath=''):
    send_to_my_file_helper(msg, imagepath)
    # send_to_group(msg, imagepath)
   