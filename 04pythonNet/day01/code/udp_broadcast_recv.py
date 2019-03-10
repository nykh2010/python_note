# udp_broadcast_recv.py


# 接收广播
from socket import *
# 1. 创建UDP套接字
udp_recv = socket(AF_INET, SOCK_DGRAM)
# 2. 为接收广播把套接字广播的选项打开
udp_recv.setsockopt(SOL_SOCKET,
                    SO_BROADCAST,1)
# 3. 绑定地址:
udp_recv.bind(("0.0.0.0", 9999))

# 4. 接收广播
while True:
    try:
        recv_bytes, addr = udp_recv.recvfrom(1024)
        recv_str = recv_bytes.decode()  # 转为字符串
        print("接收到IP地址为:", addr[0],
              '的主机发出广播', recv_str)
    except InterruptedError:  # 当ctrl + c 中断时
        break
# 5. 关闭套接字
udp_recv.close()
