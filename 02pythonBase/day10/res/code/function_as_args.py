def f1():
    print("f1被调用")

def f2():
    print("f2被调用")

def fx(fn):
    print(fn)
    fn()  # 调用形参fn绑定的函数

fx(f1)  # 将函数f1传入了fx中
fx(f2)  