# tcp_client.py

# 此示例示意TCP传输入客户端套接字创建流程和数据传送方式

# 1. 创建套接字(socket.socket)
from socket import *
tcp_client = socket()  # 创建TCP通信的套接字

# 2. 请求连接服务器 connect
print("准备连接.....")
addr = ('127.0.0.1', 8888)
# input("请输回键调用connect")
tcp_client.connect(addr)

# 3. 收发数据消息(recv/send)
s = input("请输入要给服务器发送的信息: ")  # 阻塞函数
send_bytes = s.encode()  # 转为字节串
count = tcp_client.send(send_bytes)
print("已成功发送给服务器端", count, '个字节')

print("等待服务器端返回信息给我(客户端)....")
recv_bytes = tcp_client.recv(1024)
print("收到服务器发来的信息:", recv_bytes.decode())

# 4. 关闭套接字(close)
tcp_client.close()


