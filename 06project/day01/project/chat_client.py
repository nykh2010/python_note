from socket import * 
import os,sys 

ADDR = ('127.0.0.1',8888)

def send_msg(s,name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = 'quit'
        #输入quit表示客户端要退出聊天
        if text == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,text) 
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        if data.decode() == 'EXIT':
            os._exit(0)
        print(data.decode()+"\n发言:",end='')

#创建套接字
def main():
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        #等待回应
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break 
        else:
            print(data.decode())
    
    #创建父子进程
    pid = os.fork()
    if pid < 0:
        print("Process error")
        return 
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)

if __name__ == "__main__":
    main()