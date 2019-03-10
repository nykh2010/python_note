# tcp_server_select.py
# 此示例示意用select io 多路复用实现tcp服务器

from socket import *
from select import *  # 用于IO多路复用

tcp_server = socket()
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server.bind(('0.0.0.0', 8888))
tcp_server.listen()

# 设置一个读取列,用于把所有输入事件的IO存放起来等待监控
rlist = [tcp_server]  

while True:
    print("select...")
    # 监控rlist内的所有输入事件
    # print('rlist=', rlist)
    print("len(rlist)=", len(rlist))
    rs, ws, xs = select(rlist, [], [], 5)  # 设置最长等待时间为5s
    # if not (rs or ws or xs): # 判断是否为超时解除阻塞    
    if rs == [] and ws == [] and xs == []:
        print('timeout...')
    # 查看rs 中所有元素,对所有元素进行处理
    for a_io in rs:
        # 当这个io正好是tcp_server时,说明有客户端连接
        if a_io is tcp_server:
            # 此时的accept将不再是阻塞函数,因为此io已有数据
            # 需要处理
            u_socket, u_addr = tcp_server.accept()
            # 同时让客户端套接字加入监控列表
            rlist.append(u_socket)
        else: # 直到此处一定是客户端io
            # 接收客户端数据
            recv_byte = a_io.recv(4096)
            if not recv_byte:  # 客户端断开连接
                rlist.remove(a_io)  # 将此io移出监控列表
                a_io.close()  # 关闭套接字
                continue
            recv_str = recv_byte.decode()
            print("客户端,", a_io.getpeername(),
                  '的数据是:', recv_str)
            send_str = '====' + recv_str + '===='
            a_io.send(send_str.encode())


tcp_server.close()  # 此语句永远不会执行














