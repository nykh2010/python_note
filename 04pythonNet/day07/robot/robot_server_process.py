# robot_server_select.py

# 自动聊天机器人的实现原型(TCP协议)
# 2. 改为多进程实现

import socket
from multiprocessing import Process
import time

tcp_server = socket.socket()
tcp_server.setsockopt(socket.SOL_SOCKET,
                      socket.SO_REUSEADDR, 1)
tcp_server.bind(("0.0.0.0", 8888))
tcp_server.listen()

count = 0

def task(user_sock):  # user_sock绑定用户套接字
    while True:
        data = user_sock.recv(1024)
        if data:
            send_data = b'===='+data+b'===='
            time.sleep(5)
            user_sock.send(send_data)
        else:
            user_sock.close()  # 断开连接
            break  # 退出进程或线程

tasks = []
while True:
    print("等待客户端连接...")
    user_sock, addr = tcp_server.accept()
    count += 1
    print("接收客户端连接", addr, '人数是:', count)
    t = Process(target=task, args=(user_sock,))
    t.start()
    tasks.append(t)



tcp_server.close()
print("服务器正常退出")


