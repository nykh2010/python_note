#coding=utf-8
'''
ftp文件服务器
fork server 
'''

from socket import * 
import os,sys 
import time 
import signal

#全局变量
HOST = '0.0.0.0'
PORT = 8888 
ADDR = (HOST,PORT)
FILE_PATH = "/home/tarena/ftpFile/"

class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        #获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return 
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files += file + ','
        #将拼接的大字符串发送
        self.connfd.send(files.encode())
    
    def do_get(self,filename):
        try:
            fd = open(FILE_PATH+filename,'rb')
        except IOError:
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        
        #发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break 
            self.connfd.send(data)

    def do_put(self,filename):
        try:
            fd = open(FILE_PATH+filename,'wb')
        except IOError:
            self.connfd.send("上传失败".encode())
            return
        else:
            self.connfd.send(b'OK')
        #接受文件
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break 
            fd.write(data)
        fd.close()
#创建网络连接
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(3)
    print("Listen the port 8888...")

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception:
            print("服务器异常:",e)
            continue
        print("连接客户端:",addr)

        #创建子进程
        pid = os.fork()
        if pid == 0:
            #处理具体的客户端事物
            sockfd.close()
            ftp = FtpServer(connfd)
            while True:
                data = connfd.recv(1024).decode()
                if not data or data[0] == 'Q':
                    connfd.close()
                    break
                elif data[0] == 'L':
                    ftp.do_list()
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)
                elif data[0] == 'P':
                    filename = data.split(' ')[-1]
                    ftp.do_put(filename)
            os._exit(0)
        else:
            connfd.close()

if __name__ == "__main__":
    main()




