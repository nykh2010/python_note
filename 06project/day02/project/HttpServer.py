#coding=utf-8
'''
http server
'''

from socket import *
from threading import Thread 
from settings import *

#和webframe交互
def connect_frame(request_type,path_info):
    s = socket()
    try:
        s.connect(frame_address)
    except Exception as e:
        print(e)
        return
    request = request_type + ' '+path_info
    s.send(request.encode())
    response = s.recv(4096).decode()
    return response

class HTTPServer(object):
    def __init__(self,address):
        self.address = address 
        self.create_socket()
        self.bind(address)
    #创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,\
            SO_REUSEADDR,1)
    
    #绑定地址
    def bind(self,address):
        self.ip = address[0]
        self.port = address[1]
        self.sockfd.bind(address)

    #启动服务
    def serve_forever(self):
        self.sockfd.listen(10)
        print("Listen the port %d..."%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print("Connect from",addr)
            handle_client=Thread(target=self.handle,\
                args=(connfd,))
            handle_client.setDaemon(True)
            handle_client.start()
    
    def handle(self,connfd):
        request = connfd.recv(4096)
        if not request:
            connfd.close()
            return 
        request_lines = request.splitlines()
        requestLine = request_lines[0].decode()
        print(requestLine)
        
        env = requestLine.split(' ')[:2]
        response = connect_frame(*env)
        self.send_response(connfd,response)
    
    def send_response(self,connfd,response):
        if response == '404':
            response_headlers = "HTTP/1.1 404 Not Found\r\n"
            response_headlers+='\r\n'
            response_body = "Sorry not found"
        else:
            response_headlers = "HTTP/1.1 200 OK\r\n"
            response_headlers+='\r\n'
            response_body = response
        
        response = response_headlers + response_body
        connfd.send(response.encode())

if __name__ == "__main__":
    httpd = HTTPServer(ADDR)
    httpd.serve_forever() #启动服务

