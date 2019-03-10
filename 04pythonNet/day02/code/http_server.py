# http_server.py


# 此示例示意用当前程序作为网站的服务器示意


from socket import *
tcp_server = socket()  # 创建TCP套按字

tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

tcp_server.bind( ('0.0.0.0', 80) )

tcp_server.listen()

while True:  # 用循环方式处理多个用户的连接
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
        # print("收到客户端的信息是:", user_data)
        print("收到客户端的信息是:", user_data.decode())
        user_socket.send(b'hello')
        # 主动断开连接
        user_socket.close()  # 申请断开连接

# 6. 关闭套接字(close)
tcp_server.close()  # 释放套接字资源
