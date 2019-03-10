# 练习:
#   1. 求 1**2 + 2**2 + 3**2 + ..... + 9**2 的和
# def f1(x):
#     return x ** 2

# print(sum(map(f1, range(1, 10))))
print(sum(map(lambda x: x**2, range(1, 10))))

#   2. 求 1**3 + 2**3 + 3**3 + ..... + 9**3 的和
print(sum(map(lambda x: x**3, range(1, 10))))

#   3. 求 1**9 + 2**8 + 3**7 + ......+ 9**1 的和
print(sum(map(lambda x, y: x**y, range(1, 10), range(9, 0, -1))))



