# tcp_client2.py


# 此示例示意TCP的字节流协议,客户端发送两个或两个以
# 上的数据包, 服务器端可能会一次性收到(没有边界)


# 1. 创建套接字(socket.socket)
from socket import *
tcp_client = socket()  # 创建TCP通信的套接字

# 2. 请求连接服务器 connect
print("准备连接.....")
addr = ('127.0.0.1', 8888)
# input("请输回键调用connect")
tcp_client.connect(addr)

# 3. 收发数据消息(recv/send)
input("准备发送两个数据包,按回车键开始: ")  # 阻塞函数

tcp_client.send(b'Hello')
tcp_client.send(b'world')

recv_bytes = tcp_client.recv(1024)
print("服务器说:", recv_bytes.decode())


# 4. 关闭套接字(close)
tcp_client.close()


