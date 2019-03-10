# robot_server_select.py

# 自动聊天机器人的实现原型(TCP协议)
# 1. 用IO多路复用 select实现(单进程，单线程)

import socket
import select

tcp_client = socket.socket()
# tcp_client.connect(("172.0.0.1", 8888))  # 本机测试
tcp_client.connect(("172.40.91.159", 8888))
while True:
    s = input("请输入要发送给机器的话: ")
    if not s:
        break
    b = s.encode()
    tcp_client.send(b)
    recv_bytes = tcp_client.recv(1024)
    print("机器人说:", recv_bytes.decode())


