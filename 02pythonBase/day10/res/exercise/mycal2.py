# 写一个计算公式的解释执行器
#   已知有下列一些函数:
#     def myadd(x, y):
#         return x + y

#     def mysub(x, y):
#         return x - y

#     def mymul(x, y)
#         return x * y
#   有一个函数 get_op(x) 此函数定义如下:
#     def get_op(x):
#         .... # 此处自己实现
#     此函数传入"加" 返回 myadd函数
#     此函数传入"减" 返回 mysub函数
#     此函数传入"乘" 返回 mymul函数
#   在主函数中程序如下:
#     def main():
#         while True:
#            s = input('请输入计算公式')  # 10 加 20
#            L = s.split()  # L = ['10', '加', '20']
#            a = int(L[0])
#            b = int(L[2])
#            fn = get_op(L[1])
#            print("结果是:", fn(a, b))  # 30
#     main()


def main():
    def get_op(x):
        if x == '加' or x == '+':
            def myadd(x, y):
                return x + y
            return myadd
        if x == '减' or x == '-':
            def mysub(x, y):
                return x - y
            return mysub
        if x == '乘' or x == '*':
            def mymul(x, y):
                return x * y
            return mymul

    while True:
       s = input('请输入计算公式: ')  # 10 加 20
       L = s.split()  # L = ['10', '加', '20']
       a = int(L[0])
       b = int(L[2])
       fn = get_op(L[1])
       print("结果是:", fn(a, b))  # 30
main()

