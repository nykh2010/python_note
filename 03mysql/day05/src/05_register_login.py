from mysqlpy import Mysqlpy
from hashlib import sha1

sqlh = Mysqlpy('db5')

menu = """(1)注册
(2)登录
(q)退出
请选择(1/2/q):"""

while True:
    choice = input(menu)
    if choice.strip() in "12q":
        if choice.strip() == "1":
            # 注册功能
            uname = input("请输入用户名:")
            sel = 'select username from user where username=%s'
            result = sqlh.all(sel,[uname])
            # result结果有2种,1种为空元组代表用户不存在,
            # 1种为非空元组,用户名已经存在
            if len(result) != 0:
                print("该用户名已存在")
            else:
                pwd1 = input("请输入密码:")
                pwd2 = input("请再次输入密码:")
                # 判断两次密码是否一致
                if pwd1 == pwd2:
                    # 给密码进行加密
                    # 1.创建sha1加密对象
                    s = sha1()
                    # 2.加密(参数要为bytes数据类型)
                    s.update(pwd1.encode("utf-8"))
                    # 3.返回十六进制加密结果
                    pwd = s.hexdigest()
                    # print(pwd)
                    # 存数据库
                    ins = 'insert into user values(%s,%s)'
                    sqlh.zhixing(ins,[uname,pwd])
                    print("恭喜你,注册成功")
                    break
                else:
                    print("两次密码不一致")
        elif choice.strip() == "2":                
            # 登录功能
            uname = input("用户名:")
            pwd = input("密码:")
            sel = 'select password from user where username=%s'
            result = sqlh.all(sel,[uname])
            # print(result)
            # (('40bd001563085fc35165329ea1ff5c5ecbdbbeef',),
            s = sha1()
            s.update(pwd.encode("utf-8"))
            pwd = s.hexdigest()

            if len(result) == 0:
                print("用户名不存在")
            elif result[0][0] == pwd:
                print("登录成功")
                break
            else:
                print("密码错误")
        else:
            print("程序退出")
            break
    else:
        print("无效的选择,请输入(1/2/q)")








