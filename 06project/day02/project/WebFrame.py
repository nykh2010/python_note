#coding=utf-8
'''
模拟web框架部分
'''
from socket import *
from select import select
from views import *

#配置框架地址
frame_ip = '127.0.0.1'
frame_port = 8080
frame_address = (frame_ip,frame_port)

#静态网页目录
STATIC_DIR = './static'

#可以获取的数据列表
urls = [
    ('/time',show_time),
    ('/hello',say_hello),
]

#应用类，将功能封装
class Application(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,\
            SO_REUSEADDR,1)
        self.sockfd.bind(frame_address)
        self.rlist = [self.sockfd]
        self.wlist = []
        self.xlist = []
    
    def start(self):
        self.sockfd.listen(5)
        print("Listen the port 8080")
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    request = r.recv(1024).decode()
                    if not request:
                        self.rlist.remove(r)
                        connfd.close()
                        continue
                    self.handle(r,request)
    
    def handle(self,connfd,request):
        request_type = request.split(' ')[0]
        path_info = request.split(' ')[1]
        if request_type == 'GET':
            if path_info=='/' or path_info[-5:]=='.html':
                self.get_html(connfd,path_info)
            else:
                self.get_data(connfd,path_info)
        elif request_type == 'POST':
            pass
    
    def get_html(self,connfd,path_info):
        if path_info == '/':
            get_file = STATIC_DIR + '/index.html'
        else:
            get_file = STATIC_DIR + path_info
        try:
            fd = open(get_file)
        except IOError:
            response = '404'
        else:
            response = fd.read()
        finally:
            connfd.send(response.encode())
    
    def get_data(self,connfd,path_info):
        for url,func in urls:
            if path_info == url:
                response = func()
                break
        else:
            response = '404'      
        connfd.send(response.encode())
        

if __name__ == "__main__":
    app = Application()
    app.start() #启动框架程序



