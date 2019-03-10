# namespace.py

# 此示例示意作用域
v = 100  # 全局变量
def fun1():
    v = 200
    print("fun1.里的v=", v)
    def fun2():
        v = 300
        print('fun2里的v=', v)
    fun2()

fun1()
print("全局的v=", v)

