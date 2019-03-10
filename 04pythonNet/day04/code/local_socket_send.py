# local_socket_send.py

# 此示例示意本地套按字的发送端

# 定义两个应用约定好的通信套接字文件
# 要求此文件所在的位置，双方都有权访问
socket_file = '/home/tarena/mysock'

from socket import *

send_sock = socket(AF_UNIX, SOCK_STREAM)

send_sock.connect(socket_file)
while True:
    s = input("请输入发送给接收者的数据: ")
    if not s:
        break
    send_sock.send(s.encode())
send_sock.close()

print("程序正常退出")
