# 账户查询客户端
''' 数据格式：
查询
    请求
        query::all
        query::622345000001
    响应
        查询成功，共1笔记录
        账号：622345000001, 户名：Jerry, 余额：1000

新建
    请求
        new::622345000005::Dekie::1::10.00
    响应
        操作结果，影响1行
'''
from socket import  *
import  pymysql

client = None
svr_host = "127.0.0.1"
svr_port = 9999

def print_menu():
    "打印菜单"
    menu = '''
    ------------ 账户管理系统 ---------------
        1 - 查询账户信息
        2 - 新建账户
        3 - 修改账户
        4 - 删除账户
        5 - 退出
    '''
    print(menu)
    return

def open_conn():
    "连接到服务器"
    try:
        global client
        client = socket()
        client.connect((svr_host, svr_port))
        print("连接服务器成功")
        return 0
    except:
        print("连接服务器失败")
        return -1

def close_conn():
    "关闭服务器连接"
    if not client:
        return
    else:
        client.close()

def query_acct():
    "查询账户信息"
    acct_no = input("请输入账号:")
    if acct_no and acct_no != "":
        msg = "query::" + acct_no  # 根据账号查询
    else:
        msg = "query::all"  # 查询所有账户信息

    if send_msg(msg) < 0: # 发送查询请求
        print("发送失败")
        return

    data = recv_msg()   # 接受结果
    if not data:
        print("接收失败")
    else:
        print(data.decode()) # 打印结果

    return

def new_acct():
    "新建账户信息"
    try:
        acct_no = input("请输入账号:")
        acct_name = input("请输入户名:")
        acct_type = input("请输入账户类型(1-借记卡 2-理财卡  3-代缴代扣卡)：")
        balance = float(input("请输入开户金额:"))
        assert acct_type in ["1", "2", "3"]
        assert balance >= 0.000001
    except ValueError:
        print("数据格式有误，请检查后重新输入")
        return
    except AssertionError:
        print("数据范围有误，请检查后重新输入")
        return
    except:
        print("输入处理错误")
        return
    else:
        msg = "new::%s::%s::%s::%.2f" % (acct_no, acct_name, acct_type, balance)
        print(msg)
        if send_msg(msg) < 0:
            pritn("发送失败")
            return
        data = recv_msg()  # 接收响应
        if not data:
            print("接收失败")
        else:
            print(data.decode())
    return

def update_acct():
    try:
        acct_no = input("请输入账号:")
        acct_name = input("请输入户名:")
        acct_type = input("请输入账户类型(1-借记卡 2-理财卡  3-代缴代扣卡)：")
        balance = float(input("请输入开户金额:"))
        assert acct_type in ["1", "2", "3"]
        assert balance >= 0.000001
    except ValueError:
        print("数据格式有误，请检查后重新输入")
        return
    except AssertionError:
        print("数据范围有误，请检查后重新输入")
        return
    except:
        print("输入处理错误")
        return
    else:
        msg = "update::%s::%s::%s::%.2f" % (acct_no, acct_name, acct_type, balance)
        print(msg)
        if send_msg(msg) < 0:
            pritn("发送失败")
            return
        data = recv_msg()  # 接收响应
        if not data:
            print("接收失败")
        else:
            print(data.decode())
    return


def delete_acct():
    acct_no = input("请输入账号:")
    if acct_no and acct_no != "":
        msg = "delete::" + acct_no  # 根据账号查询
    else:
        print("请输入合法账号")
        return

    if send_msg(msg) < 0: # 发送查询请求
        print("发送失败")
        return

    data = recv_msg()   # 接受结果
    if not data:
        print("接收失败")
    else:
        print(data.decode()) # 打印结果

    return

def send_msg(msg):
    global client
    if not client:
        return -1
    if not msg:
        return -1
    if msg == "":
        return -1
    n = client.send(msg.encode())
    return n

def recv_msg():
    global client
    if not client:
        return -1

    data = client.recv(2048)

    return data

def main():
    "主函数"
    open_conn()
    while True:
        print_menu()
        oper = input("请选择操作:")
        if not oper:
            continue
        if oper == "1": # 查询
            query_acct()
        elif oper == "2":# 新建
            new_acct()
        elif oper == "3":#修改
            update_acct()
        elif oper == "4": #删除
            delete_acct()
        elif oper == "5": #退出
            break
        else:
            print("请输入正确的值")
            continue
    close_conn()
    return

main()