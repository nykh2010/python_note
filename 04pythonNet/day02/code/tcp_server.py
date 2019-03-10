# tcp_server.py

# 1. 创建套接字(socket.socket)
from socket import *
tcp_server = socket()  # 创建TCP套按字

# 2. 绑定地址(bind)
tcp_server.bind( ('0.0.0.0', 8888) )

# 3. 设置监听(listen)
tcp_server.listen()

# 4. 等待处理客户端请求连接(accept)
print("正在等待用户连接....")
client = tcp_server.accept()  # 阻塞函数 
user_socket, user_addr = client  # 序列赋值
print("已接收IP地址为:%s, 端口号为%d" % user_addr, 
      '的客户端连接')

# 5. 收发数据消息(recv/send)
# 注: 用accept返回的套接与客户端进行通信
print("等待客户端发消息给我.....")
user_data = user_socket.recv(1024)  # 阻塞函数
# 如果收到的是空字节串,说明客端准备断开连接
if user_data == b'':
    print("客户端:", user_addr, '已断开连接')
else:
    print("收到客户端的信息是:", user_data)
    send_bytes = '服务器收到的是:'.encode() + \
                 user_data
    user_socket.send(send_bytes)
    # 主动断开连接
    user_socket.close()  # 申请断开连接

# 6. 关闭套接字(close)
tcp_server.close()  # 释放套接字资源
