# 学生信息管理程序网络版，　TCP协议实现

# 此为客户端　

from socket import *

def show_menu():
    print("1) 添加")
    print("2) 删除")
    print("3) 显示")
    print("q) 退出")


# 发送:
# "1{'name':'xiaozhang', 'age':20, 'score:100'}"
# 接收:
# "1ok" 或"1failed"

def add_student(sockfd):
    n = input("请输入姓名: ")
    a = input("请输入年龄: ")
    s = input("请输入成绩: ")
    d = dict(name=n, age=a, score=s)
    send_str = str(d)  # 把字典转为字符串准备发送
    package = '1' + send_str  # 1为协议表示添加
    sockfd.send(package.encode())  # 发送字节串
    recv_bytes = sockfd.recv(4096)  # 接收结果
    recv_str = recv_bytes.decode()
    if recv_str[0] == '1':
        if recv_str[1:] == 'ok':
            print("添加成功")
        else:
            print("添加失败")

def del_student(sockfd):
    pass

# 发送: '3'
# 接收:"3[字典的列表]"
def show_all_student(sockfd):
    sockfd.send('3'.encode())
    recv_bytes = sockfd.recv(4096)
    recv_str = recv_bytes.decode()
    if recv_str[0] == '3':
        list_infos = eval(recv_str[1:])
    print('list_infos=', list_infos)

def main():
    tcp_socket = socket()

    server_addr = ('127.0.0.1', 8888)
    tcp_socket.connect(server_addr)
    while True:
        show_menu()
        s = input("请选择:　")
        if s == '1':
            add_student(tcp_socket)
        elif s == '2':
            del_student(tcp_socket)
        elif s == '3':
            show_all_student(tcp_socket)
        elif s == 'q':
            break
    tcp_socket.close()

main()
