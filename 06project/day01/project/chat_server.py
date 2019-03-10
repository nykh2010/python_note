#coding=utf-8
'''
Chatroom
env:Python3.5
socket and fork 
'''

from socket import *
import os,sys

#存放用户 存储结构  {'zhangsan':('127.0.0.1',8888)}
user = {}

#处理用户进入聊天室
def do_login(s,name,addr):
    if (name in user) or name == "管理员消息":
        s.sendto("\n该用户已存在".encode(),addr)
        return
    else:
        s.sendto(b'OK',addr)
    
    #通知其他人
    msg = "\n欢迎 %s 进入聊天室"%name 
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入user
    user[name] = addr 

def do_chat(s,name,text):
    msg = "\n%s : %s"%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])    

def do_quit(s,name):
    msg = "\n%s 退出聊天室"%name
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    #删除用户
    del user[name]
    

#处理请求
def do_request(s):
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')
        if msgList[0] == 'L':
            do_login(s,msgList[1],addr) 
        elif msgList[0] == 'C':
            text = ' '.join(msgList[2:])
            do_chat(s,msgList[1],text)
        elif msgList[0] == 'Q':
            do_quit(s,msgList[1])

#创建网络连接
def main():
    ADDR = ('0.0.0.0',8888)
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    #创建父子进程，用于处理客户端请求和发送管理员消息
    pid = os.fork()
    if pid < 0:
        print("Process error")
        return
    elif pid == 0:
        #准备发送管理员消息
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息 " + msg
            s.sendto(msg.encode(),ADDR)
    else:
        #调用函数处理客户端请求
        do_request(s)

if __name__ == "__main__":
    main()