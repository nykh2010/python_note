# local_socket_recv.py

# 此示例示意本地套接字的接收端

# 定义两个应用约定好的通信套接字文件
# 要求此文件所在的位置，双方都有权访问
socket_file = '/home/tarena/mysock'

# 创建本地套接字
from socket import *
recv_socket = socket(AF_UNIX, SOCK_STREAM)
recv_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 绑定路径：用路径来确认通信地址
recv_socket.bind(socket_file)

# 监听
recv_socket.listen()

while True:
    # 接收发送端连接
    print("accept...")
    user_socket, addr = recv_socket.accept()
    print("发送端:", addr, "已连接")
    while True:
        # 接收数据
        recv_bytes = user_socket.recv(4096)
        if not recv_bytes:
            break
        print("已收到:", recv_bytes.decode())

recv_socket.close()
print("程序正常退出")
