# closure2.py


def get_fx(a, b, c):
    # 定义一个闭包,用来生成f(x) = ax2 + bx + c的曲线
    def fx(x):
        return a * x ** 2 + b * x + c
    return fx


f123 = get_fx(1, 2, 3)  # f123绑定y=x2+2x+3 函数
print('y = ', f123(10))


f456 = get_fx(4, 5, 6)  # f123绑定y=4x2+5x+6 函数
print('y = ', f456(20))



