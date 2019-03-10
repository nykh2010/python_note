# udp_broadcast_sender.py

from socket import *
# 1. 创建UDP套接字
udp_sender = socket(AF_INET, SOCK_DGRAM)
# 2. 为发送/接收广播设置此套接字选项
udp_sender.setsockopt(SOL_SOCKET,
                      SO_BROADCAST,
                      1)
# 3. 定时发送广播信息
broadcast_addr = ("172.40.91.255", 9999)
import time
for x in range(100):
    time.sleep(2)  # 停两秒
    udp_sender.sendto("北京天冷多穿点!".encode(),
        broadcast_addr)
    print("已成功发送!")

udp_sender.close()  # 关闭套接字，释放资源



