# 3. 给出一个数n, 写一个函数 计算:
#    1 + 2**2 + 3**3 + .... n**n的和


# def fn(n):
#     s = 0
#     for i in range(1, n + 1):
#         s += i ** i
#     return s

def fn(n):
    return sum(map(lambda x: x ** x, range(1, n + 1)))

print(fn(3))