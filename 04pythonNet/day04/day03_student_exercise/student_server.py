# 学生信息管理程序网络版，　TCP协议实现

# 此为服务端　

from socket import *
from select import *


# 发送:
# "1{'name':'xiaozhang', 'age':20, 'score:100'}"
# 接收:
# "1ok" 或"1failed"

infos = []  # 列表用于存存学生信息

def addition(client_sock, s):
    print("正在添加", s)
    try:
        d = eval(s)  # 把字符串转为字典
        infos.append(d)
        client_sock.send('1ok'.encode())
    except:
        client_sock.send('1failed')

    print(infos)

def request_list(client_sock):
    s = '3' + str(infos)
    client_sock.send(s.encode())

def main():

    tcp_socket = socket()
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_addr = ('0.0.0.0', 8888)
    tcp_socket.bind(server_addr)
    tcp_socket.listen()

    # 列表用于维护所有IO
    rlist = [tcp_socket]
    while True:
        print("select...")
        rs, ws, xs = select(rlist, [], [])
        for io in rs:
            if io is tcp_socket:
                u_socket, u_addr = tcp_socket.accept()
                rlist.append(u_socket)
            else:
                # 客户端发消息给服务端
                recv_bytes = io.recv(4096)
                if not recv_bytes:
                    io.close()
                    rlist.remove(io)
                    continue
                recv_str = recv_bytes.decode()
                if recv_str[0] == '1': # 添加学生信息
                    addition(io, recv_str[1:])
                elif recv_str[0] == '3':  # 请求学生信息列表
                    request_list(io)








    tcp_socket.close()

main()
