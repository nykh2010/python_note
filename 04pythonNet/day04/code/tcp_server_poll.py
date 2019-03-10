# tcp_server_poll.py

# 此示例示意用poll方式实现TCP服务器

from socket import *
from select import *  # poll 在select模块内

tcp_server = socket()  # 第一个IO
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_addr = ('0.0.0.0', 8888)
tcp_server.bind(server_addr)
tcp_server.listen()

# 创建一个字典,此字典用于映射所有文件描述符和IO的对应关系
fd_dict = {tcp_server.fileno(): tcp_server}

# 创建poll 对象
poll_obj = poll()

# 将tcp_server 套接字注册到poll中,让poll进行关注,
# 只关注POLLIN(当有客户端进行连接时)
poll_obj.register(tcp_server.fileno(), POLLIN)

while True:
    print("poll...")
    events = poll_obj.poll()  # 等待IO事件发生
    print("events=", events)
    for fd, event in events:  # 遍历所有已经发生IO事件的IO
        a_io = fd_dict[fd]  # 根据fd查找到IO对象
        if a_io is tcp_server:
            user_socket, useraddr= a_io.accept()  # 接收客户端连接
            print("有客户端连接:", useraddr)
            # 让poll 关注此user_socket对象,关注:
            # 断开事件POLLHUP和 输入事件POLLIN
            poll_obj.register(user_socket,
                     POLLIN | POLLHUP)
            # 把当前的文件描述符的IO对象加入到字典中
            fd_dict[user_socket.fileno()] = user_socket
        elif event & POLLHUP:  # 判断是否是连接断开
            client_addr = a_io.getpeername()
            print("用户断开连接", client_addr)
            # 取消poll 关注
            poll_obj.unregister(fd)
            a_io.close()  # 关闭套按字
            del fd_dict[fd]  # 从字典中删除此fd
        elif event & POLLIN: # 客户端发来数据
            data = a_io.recv(4096)
            recv_str = data.decode()
            print("收到客户端消息:", recv_str)

            send_str = "====" + recv_str + '===='
            # 给客户端回消息
            a_io.send(send_str.encode())

tcp_server.close()
print("程序正常退出")







