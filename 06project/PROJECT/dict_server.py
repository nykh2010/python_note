'''
dict exc
'''
from socket import *
import pymysql 
import os 
import sys 
import signal 
import time 

#定义需要的全局变量
DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8000 
ADDR = (HOST,PORT)

#网络搭建
def main():
    #创建数据库连接
    db = pymysql.connect('localhost','root',\
        '123456','dict')
    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue 
        
        #创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c,db)  #处理客户端请求
            os._exit(0)
        else:
            c.close()

def do_child(c,db):
    while True:
        #接收客户端请求
        data = c.recv(128).decode()
        print(c.getpeername(),":",data)
        if not data or data[0] == 'E':
            c.close()
            sys.exit()
        elif data[0] == 'R':
            do_register(c,db,data)
        elif data[0] == 'L':
            do_login(c,db,data)
        elif data[0] == 'Q':
            do_query(c,db,data)
        elif data[0] == 'H':
            do_hist(c,db,data)

def do_register(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql="select * from user where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()

    if r != None:
        c.send(b'EXISTS')
        return 
    
    #插入数据
    sql="insert into user (name,passwd) values \
        ('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send(b'FAIL')

def do_login(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql="select * from user where \
        name='%s' and passwd='%s'"%(name,passwd)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FAIL')
    else:
        c.send(b'OK')

def do_query(c,db,data):
    l = data.split(' ')
    name = l[1]
    word = l[2]
    cursor = db.cursor()

    tm = time.ctime()
    sql = "insert into hist (name,word,time)\
         values ('%s','%s','%s')"%(name,word,tm)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    #使用文本
    try:
        f = open(DICT_TEXT)
    except IOError:
        c.send(b"FALL")
        return 
    for line in f:
        tmp = line.split(' ')[0]
        if tmp > word:
            break
        elif tmp == word:
            c.send(line.encode())
            f.close()
            return 
    c.send("没有该单词".encode())
    f.close()

def do_hist(c,db,data):
    l = data.split(' ')
    name = l[1]
    cursor = db.cursor()

    sql="select * from hist where \
        name='%s' limit 10"%name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send(b'FAIL')
        return
    else:
        c.send(b'OK')
        time.sleep(0.1)
    for i in r:
        msg="%s    %s    %s\n"%(i[1],i[2],i[3])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'##')

if __name__ == "__main__":
    main()