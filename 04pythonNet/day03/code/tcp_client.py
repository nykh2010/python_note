# tcp_client.py

from socket import *
tcp_client = socket()

# server_addr = ('127.0.0.1', 8888)
server_addr = ('172.40.91.159', 8888)
tcp_client.connect(server_addr)

while True:
    s = input("请输入要发送的文字: ")
    if not s:  # 与服务器交换数据结束
        break
    send_bytes = s.encode()
    tcp_client.send(send_bytes)
    recv_bytes = tcp_client.recv(4096)
    recv_str = recv_bytes.decode()
    print("收到服务器信息:", recv_str)


tcp_client.close()

