# 账户查询客户端
from socket import  *
import pymongo

#修改地址
db_host = "127.0.0.1"
db_port = 27017
db_name = "test"

svr_host = "0.0.0.0"
svr_port = 9999

db_conn = None   # 数据连接对象

def conn_database():
    global db_conn
    db_conn = pymongo.MongoClient(db_host, db_port)
    if not db_conn:
        print("连接数据库失败")
        return -1
    else:
        return 1

def close_database():
    global db_conn
    if not db_conn:
        return
    else:
        db_conn.close()

def query(msgs):#修改整个函数
    qry = ""
    if msgs[1] == "all":
        qry = {}
    else:
        qry = {"acct_no": msgs[1]} 

    print(qry)

    resp = ""
    try:
        dblist = db_conn.list_database_names()
        if db_name in dblist:
            mydb = db_conn[db_name]
            mycol = mydb["acct"]

            docs = mycol.find(qry) #执行查询
            
            for doc in docs:
                acct_info = "账户:%s, 户名:%s, 余额:%f\n" % \
                             (doc["acct_no"], doc["acct_name"], doc["balance"])
                resp += acct_info 
    except Exception as e:
        print(e)
        print("查询异常")

    return resp

def delete_acct(msgs):#修改整个函数
    qry = ""
    qry = {"acct_no": msgs[1]} 

    print(qry)

    resp = ""
    try:
        mydb = db_conn[db_name]
        mycol = mydb["acct"]

        result = mycol.delete_one(qry) #执行查询
        resp = "共删除%d笔数据" % result.deleted_count
    except Exception as e:
        print(e)
        resp = "查询异常"

    return resp

def new_acct(msgs): #修改整个函数
    ret = ""
    acct_no = msgs[1]
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = msgs[4]
    # 组建字典
    acct_info = {
        "acct_no": acct_no,
        "acct_name": acct_name,
        "acct_type": acct_type,
        "balance": float(balance)
    }

    print(acct_info)

    try:
        dblist = db_conn.list_database_names()
        if db_name in dblist:
            mydb = db_conn[db_name]
            mycol = mydb["acct"]

            result = mycol.insert_one(acct_info)
            print("NewID:", result.inserted_id)
            ret = "插入成功，插入文档ID:%s" % result.inserted_id
    except Exception as e:
        ret = "插入文档失败"
        print(ret)

    return ret

def update_acct(msgs): #修改账户信息
    ret = ""
    acct_no = msgs[1]
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = float(msgs[4])
    
    query = {"acct_no":acct_no}
    new_values = {"$set": {"acct_name":acct_name, "acct_type":acct_type,"balance":balance} }

    try:
        mydb = db_conn[db_name]
        mycol = mydb["acct"]

        result = mycol.update_one(query, new_values)
        ret = "共修改%d笔数据" % result.modified_count
    except Exception as e:
        print(e)
        ret = "修改文档失败"

    return ret

def main():
    "主函数"
    if conn_database() < 0:  #打开数据库连接
        return

    # 启动网络服务器
    server = socket()
    server.bind((svr_host, svr_port))
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.listen(5)
    print("服务器已启动:", (svr_host, svr_port))

    sockfd, addr = server.accept()

    while True:
        data = sockfd.recv(2048)  #接收数据
        if not data:
            print("客户端已关闭")
            break

        # 解析、分发
        print(data.decode())
        msgs = data.decode().split("::")
        if msgs[0] == "query":  #查询
            result = query(msgs)
        elif msgs[0] == "new": #新增
            result = new_acct(msgs)
        elif msgs[0] == "update": #修改
            result = update_acct(msgs)
        elif msgs[0] == "delete": #删除
            result = delete_acct(msgs)
        else:
            print("非法的操作请求")
            continue

        sockfd.send(result.encode())  # 发送结果

    close_database() #管理数据库连接
    return

main()
