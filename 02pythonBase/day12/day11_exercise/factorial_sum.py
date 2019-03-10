# 3. 写程序算出 1 ~ 20 的阶乘的和
#    1! + 2! + 3! + 4! + ..... + 20!

# 方法1
# def myfac(n):
#     if n == 1:
#         return 1
#     return n * myfac(n - 1)
# s = 0
# for x in range(1, 21):
#     s += myfac(x)

# print(s)

import math

print(sum(map(math.factorial, range(1, 21))))
