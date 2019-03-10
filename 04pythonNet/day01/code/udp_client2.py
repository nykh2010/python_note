# udp_client.py

# 此示例示意UDP客户端的用法

# 四步
from socket import *
# 1. 创建套接字
udp_client = socket(AF_INET, SOCK_DGRAM)
# 2. 绑定(略)
# 3. 发送/接收数据
server_addr = ("127.0.0.1", 8888)
# server_addr = ("172.40.91.145", 8888)
while True:
    s = input("请输入要发送给服务器的数据: ")
    if not s:
        break
    send_bytes = s.encode()  #  转为字节串
    n = udp_client.sendto(send_bytes, server_addr)
    print("您已成功发送",n , "个字节")
    recv_bytes, addr = udp_client.recvfrom(1024)
    recv_str = recv_bytes.decode()
    print("收到来自服务器的数据:", recv_str)
    print("addr=", addr)

# 4. 关闭套接字
udp_client.close()
