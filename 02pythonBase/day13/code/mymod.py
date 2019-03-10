# mymod.py

'''这是模块的文档字符串

以下用来测试自定义模块
'''

# 此示例示意自定义模块
def mysum(n):
    print('正在计算1 + 2 + 3 + ... + n的和 ')
    print("计算完毕")

def myfac(n):
    print("正在计算", n, '的阶乘')

name1 = "BYD"
name2 = "BMW"

print("mymod模块已被加载")


print("__name__属性绑定的值是:", __name__)

if __name__ == '__main__':
    print("当前模块正在以主模块运行")
    mysum(100)
else:
    print("当前模块不是主模块在运行，而是被其它模块导入的模块")

