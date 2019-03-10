# udp_server.py


#此示例示意创建UDP server

# 四步

import socket
# 1. 创建套接字
udp_server = socket.socket(socket.AF_INET,
    socket.SOCK_DGRAM, 0)  # 第三个参数可以不写
# 2. 绑定
# server_addr = ("172.40.91.145", 8888)
# server_addr = ("127.0.0.1", 8888)
server_addr = ("0.0.0.0", 8888)  # 本机全部IP地址
udp_server.bind(server_addr)
# 3. 发送和接收
  # 接收用户发来的数据,左右各加四个等号'===='再返回客户端
while True:
    print("正在等待接收数据...")  
    t = udp_server.recvfrom(1024)
    recv_bytes, client_addr = t
    print("接到IP地址为%s,端口号为:%d发来的UDP数据包" 
           % client_addr)
    print("内容是:", recv_bytes)
    send_bytes = b'====' + recv_bytes + b'===='
    udp_server.sendto(send_bytes, client_addr)

# 4. 关闭套接字
udp_server.close()



