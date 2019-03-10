# tcp_server_nonblock.py

# 此示例示意非阻塞的方式实现TCP服务器
# 此服务器将能同时对多个客户端进行服务

#　创建tcp的服务器
from socket import *

# 1. 创建套接字
tcp_server = socket()
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 2. bind
server_addr = ('0.0.0.0', 8888)
tcp_server.bind(server_addr)

# 3. listen
tcp_server.listen()

client_list = []  # 此列表用来保存所有的客户端和地址

# 将　tcp_server 套接字IO设置为非阻塞IO
# tcp_server.settimeout(0)  #　方法1
tcp_server.setblocking(False)


while True:
    # 4. accept
    try:
        print('accept...')
        auser_tuple = tcp_server.accept()  # (用户套接字, 地址信息(ip, port))
        client_list.append(auser_tuple)  # 暂存在列表中
        print(auser_tuple)
        user_socket, user_addr = auser_tuple
        # 将用户套接设置为非阻塞IO
        user_socket.setblocking(False)
        print("接收到IP: %s, 端口号: %d的用户连接" %
              user_addr)
    # except timeout:
    except BlockingIOError:
        print("accept... 没有获取到数据")
    # 5. 收发消息
    # 检查所有客户端的IO是否有数据转入
    for i, auser in enumerate(client_list):
        print("recv...")
        usr_sock, user_info = auser
        try:
            recv_bytes = usr_sock.recv(4096)  # 接收消息
        except BlockingIOError:
            continue
        if not recv_bytes:  # 客户端主动断开连接
            del client_list[i] # i为列表的索引
            usr_sock.close()  # 关闭客户端套按字
            continue  # 当前套接字处理结束，轮询
        recv_str = recv_bytes.decode()  # 转为字符串
        print("客户端", user_addr, "说:", recv_str)
        send_str = '====' + recv_str + '===='
        usr_sock.send(send_str.encode())

# 6. 关闭套接字
tcp_server.close()