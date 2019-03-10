# robot_server_select.py

# 自动聊天机器人的实现原型(TCP协议)
# 1. 用IO多路复用 select实现(单进程，单线程)

import socket
import select
import time

tcp_server = socket.socket()
tcp_server.setsockopt(socket.SOL_SOCKET,
                      socket.SO_REUSEADDR, 1)
tcp_server.bind(("0.0.0.0", 8888))
tcp_server.listen()

rlist = [tcp_server]  # 用来存储IO对象
while True:
    print("等待客户端连接...")
    rs, ws, es = select.select(rlist, [], [])
    for r_socket in rs:
        if r_socket is tcp_server:
            user_sock, addr = tcp_server.accept()
            print("接收客户端连接", addr,
                   '总连接数是:', len(rlist))
            rlist.append(user_sock)
        else:
            data = r_socket.recv(1024)
            if data:
                send_data = b'===='+data+b'===='
                time.sleep(5)
                r_socket.send(send_data)
            else:
                r_socket.close()  # 断开连接
                rlist.remove(r_socket)
                print("当前连接数是:", len(rlist)-1)

tcp_server.close()
print("服务器正常退出")


