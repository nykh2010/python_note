# mydeco3.py


# 此示例示意用装饰器在不改变原有代码的基上
# 为原有项目添加新的功能

# ---  以下是小李写的装饰器
def privileged_check(fn):
    def fx(name, x):
        print("正在进行权限验正.....")
        fn(name, x)
    return fx


def message_send(fn):
    def fy(name, x):
        fn(name, x)
        print(name, '办理了', x, '元的业务,短信发送中...')
    return fy


# ---  以下是魏老师编写的代码 -----
@privileged_check
def savemoney(name, x):
    print(name, '存钱', x, '元')

@message_send
@privileged_check
def withdraw(name, x):
    print(name, '取钱', x, '元')


# ----以下是小王写的程序用来调用魏老师写的代码
savemoney("小张", 200)
savemoney('小赵', 400)
withdraw('小李', 500)

