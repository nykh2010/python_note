# mydeco1.py


# 此示例示意装饰器用来包装原来的函数
def mydeco(fn):
    def fx():
        print("---这是myfun被调用之前-----")
        fn()  # 调用被装饰的函数
        print("===这是myfun被调用之后=====")
    return fx


# @mydeco
def myfun():
    print("函数myfun被调用")


myfun = mydeco(myfun)



myfun()
# myfun()
# myfun()



