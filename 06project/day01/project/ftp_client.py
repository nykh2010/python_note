from socket import *
import sys 
import time 

ADDR = ('127.0.0.1',8888)

#具体功能类
class FtpClient(object):
    pass


#网络连接
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("Error:",e)
        return
    
    ftp = FtpClient()

    while True:
        print("\n========命令选项========")
        print("***      list       ***")
        print("***    get file     ***")
        print("***    put file     ***")
        print("***      quit       ***")
        print("=========================")
        cmd = input("输入命令>>")

        if cmd == 'list':
            ftp.do_list()
            


if __name__ == "__main__":
    main()