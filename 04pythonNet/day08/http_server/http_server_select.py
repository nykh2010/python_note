# http_server_select.py

# 此示例以IO多路复用方式实现HTTP server
from socket import *
import select

def process_client_request(client_socket):
    b = client_socket.recv(4096)  # 接收浏览器传入的数据
    print('b=', b)
    s = b.decode()
    print('s=', s)

    response = b'HTTP/1.1 404 Not Found\r\n'  # 响应行
    response += b'\r\n'  # 响应头结束
    response += b'This Page Not Found'  # 响应体
    client_socket.send(response)

    client_socket.close()

def main_task():
    server_addr = ('0.0.0.0', 8888)
    tcp_server = socket()
    tcp_server.setsockopt(SOL_SOCKET,
                          SO_REUSEADDR, 1)
    tcp_server.bind(server_addr)         
    tcp_server.listen()

    rlist = [tcp_server]  # 准备让select接收这个IO
    while True:
        print("select...")
        rs, ws, es = select.select(rlist, [],[])
        for r_sock in rs:
            if r_sock is tcp_server:
                user_socket, addr = tcp_server.accept()
                print('addr=', addr)
                rlist.append(user_socket)
            else:
                process_client_request(r_sock)
                rlist.remove(r_sock)
    tcp_server.close()

main_task()