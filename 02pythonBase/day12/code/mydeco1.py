# mydeco1.py


# 此示例示意装饰器函数的装饰语法及其原理
def mydeco(fn):
    def fx():
        print("fx被调用了")
    return fx


@mydeco
def myfun():
    print("函数myfun被调用")


# 上述@mydeco的作用是:
# myfun = mydeco(myfun)

myfun()
myfun()
myfun()



