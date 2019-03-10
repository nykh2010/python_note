# map.py


# 此示例示意用map函数创建一个能够生成整数的平方的可迭代对象

def power2(x):
    # print('x= ', x)
    return x ** 2

# 生成一个可迭代对象,此可迭代对象可以生成1~9自然数的平方
# 1 4 9 16  ... 81
for x in map(power2, range(1, 10)):
    print(x)

L = list(map(power2, range(1, 10)))
print("L =", L)


