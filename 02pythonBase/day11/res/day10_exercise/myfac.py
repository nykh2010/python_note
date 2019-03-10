# 2. 给出一个整数n,写一个函数myfac(n)计算 n! (n的阶乘)
#   n! = 1*2*3*...*n
#   如:
#     print(myfac(5))  # 120



def myfac(x):
    s = 1
    for i in range(1, x + 1):
        s *= i
    return s

print(myfac(5))  # 120