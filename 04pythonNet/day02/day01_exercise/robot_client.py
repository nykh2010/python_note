# 练习:
#   做一个网络聊天机器人:
#     机器人为服务器端:
#       问：你好   答: Hi
#       问: 你叫什么名字  答: robot
#       问: 不是以上的两种   答:我不懂你在说什么

#     客户端:
#       请输入: 你好
#       机器人回答: Hi
#       ....
#     


# 1. 建立UDP套接字
from socket import *
robot_client = socket(AF_INET, SOCK_DGRAM)

# 3. 收发数据
addr = ('127.0.0.1', 8888)
while True:
    s = input("请输入要发送给机器人的文字: ")
    if not s:
        break
    robot_client.sendto(s.encode(), addr)
    recv_bytes, _ = robot_client.recvfrom(4096)
    print("机器人说:", recv_bytes.decode())

# 4. 关闭套接字
robot_client.close()
