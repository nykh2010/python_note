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
    pass

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
            sys.eixt("服务器退出")
        except Exception:
            print("服务器异常:",e)
            continue
        print("连接客户端:",addr)

        #创建子进程
        pid = os.fork()
        if pid == 0:
            #处理具体的客户端事物
            sockfd.close()
            ftp = FtpServer()
            while True:
                data = connfd.recv(1024).decode()
                if data == 'list':
                    ftp.do_list()

            os._exit(0)
        else:
            connfd.close()

if __name__ == "__main__":
    main()




