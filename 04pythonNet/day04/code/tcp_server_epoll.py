# tcp_server_epoll.py

# 此示例示意用epoll方式实现TCP服务器端

from socket import *
from select import *  # epoll 在select模块内
import sys

tcp_server = socket()  # 第一个IO
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_addr = ('0.0.0.0', 8888)
tcp_server.bind(server_addr)
tcp_server.listen()

# 创建一个字典,此字典用于映射所有文件描述符和IO的对应关系
fd_dict = {
    tcp_server.fileno(): tcp_server,
    sys.stdin.fileno(): sys.stdin
    # 0: sys.stdin  # 把键盘输入也加入到epoll的关注
}

# 创建epoll 对象
epoll_obj = epoll()

# 将tcp_server 套接字注册到epoll中,让epoll进行关注,
# 只关注EPOLLIN(当有客户端进行连接时)
epoll_obj.register(tcp_server.fileno(), EPOLLIN)
# 将sys.stdin 加入关注
epoll_obj.register(0, EPOLLIN)
while True:
    print("epoll...")
    # 此处用try语句捕获ctrl + c ,让程序正常终止服务器
    try:
        events = epoll_obj.poll()  # 等待IO事件发生
    except KeyboardInterrupt:
        break  # 终止当前循环
    print("events=", events)
    for fd, event in events:  # 遍历所有已经发生IO事件的IO
        a_io = fd_dict[fd]  # 根据fd查找到IO对象
        if a_io is tcp_server:
            user_socket, useraddr= a_io.accept()  # 接收客户端连接
            print("有客户端连接:", useraddr)
            # 让poll 关注此user_socket对象,关注:
            # 断开事件POLLHUP和 输入事件POLLIN
            epoll_obj.register(user_socket,
                     EPOLLIN | EPOLLHUP)
            # 把当前的文件描述符的IO对象加入到字典中
            fd_dict[user_socket.fileno()] = user_socket
        elif a_io is sys.stdin:
            s = input()  # 从sys.stdin获取数据
            if s == 'exit':
                # 关闭所有的IO
                for io in fd_dict.values():
                    io.close()
                print("程序正常退出")
                sys.exit()  # 退出程序
                break
        elif event & EPOLLHUP:  # 判断是否是连接断开
            # 取消poll 关注
            epoll_obj.unregister(fd)
            a_io.close()  # 关闭套按字
            del fd_dict[fd]  # 从字典中删除此fd
        elif event & EPOLLIN: # 客户端发来数据
            data = a_io.recv(4096)
            recv_str = data.decode()
            print("收到客户端消息:", recv_str)
            send_str = "====" + recv_str + '===='
            # 给客户端回消息
            a_io.send(send_str.encode())


# 关闭所有的IO
for io in fd_dict.values():
    io.close()

# tcp_server.close()
print("程序正常退出")







