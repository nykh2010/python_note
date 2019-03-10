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
database = {
    '你好': "Hi",
    '你叫什么名字': "robot!",
    '今天吃什么?': '您请客?'
}

# 1. 建立UDP套接字
from socket import *
robot_server = socket(AF_INET, SOCK_DGRAM)

# 2. 绑定
robot_server.bind( ('0.0.0.0', 8888) )
# 3. 收发数据
while True:
    t = robot_server.recvfrom(4096)
    recv_bytes, client_addr = t
    recv_str = recv_bytes.decode()  # 转为字符串
    if recv_str in database:
        send_bytes = database[recv_str].encode
    # if recv_str == '你好':
    #     send_bytes = "Hi".encode()  # 转为字节串
    # elif recv_str == '你叫什么名字':
    #     send_bytes = "robot!".encode()
    elif recv_str == "口令:sleep":
        break
    else:
        send_bytes = '我不知道你在说什么!'.encode()
    robot_server.sendto(send_bytes, client_addr)

# 4. 关闭套接字
robot_server.close()
