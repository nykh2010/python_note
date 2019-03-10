
# 此示例以 协程gevent  方式实现 HTTP server
# from socket import *
from gevent import monkey  # 为阻塞时能让出协程
monkey.patch_all()  # 这个必须在导入socket前调用
from gevent.socket import socket
import gevent

def get_static_file(url):
    static_dir = './static'
    if url == '/':
        filename = static_dir + '/index.html'
    else:
        filename = static_dir + url
    print("filename = ", filename)
    try:
        with open(filename, 'rb') as fr:
            return fr.read()  # 如果文件存在则返回文件内容
    except OSError:
        return b''


def process_client_request(client_socket):
    request = client_socket.recv(4096)  # 接收浏览器传入的数据
    if not request:  # 断开连接
        client_socket.close()
        return
    # 按字节串换行切割，把请求行取出
    request_head = request.splitlines()  # 按'\r\n'切割
    print("请求的第一行内空是:", request_head[0].decode())
    # 取出地址URL
    url = request_head[0].split()[1].decode()
    print("URL=", url)

    data = get_static_file(url)  # 按URL读取文件内容
    if not data:  # 读取失败
        response = b'HTTP/1.1 404 Not Found\r\n'  # 响应行
        response += b'\r\n'  # 响应头结束
        response += b'This Page Not Found'  # 响应体
        client_socket.send(response)
    else:  # 读取成功
        response = b'HTTP/1.1 200 OK\r\n'
        response += b'\r\n'
        client_socket.send(response)
        client_socket.send(data)

    client_socket.close()  # 关闭客户端套按字

def main_task():
    server_addr = ('0.0.0.0', 8888)
    tcp_server = socket()
    # tcp_server.setsockopt(socket.SOL_SOCKET,
    #                       socket.SO_REUSEADDR, 1)
    tcp_server.bind(server_addr)         
    tcp_server.listen()

    # 导入多线程 
    from threading import Thread
    while True:
        user_socket, addr = tcp_server.accept()
        print('addr=', addr)
        # 创建协程greenlet对象
        p = gevent.spawn(process_client_request,
                   user_socket)
        # 在此处回收已经死了的线程 is_alive() 来判断
    tcp_server.close()

# 把主任务函数也定为协程
m = gevent.spawn(main_task)
print("协程进行等待....")
m.join()
print("程序退出")