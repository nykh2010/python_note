# primes.py
# 2. 写一个函数isprimes(x) 判断x是否为素数,如果
#  是素数返回True,否则返回False

def isprimes(x):
    if x >= 2:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True
    return False  # 当 x < 2时


# 3. 写一个函数 prime_m2n(m, n) 返回从 m开始到n
#  结束范围内的素数,返回这些素数的列表,并打印这些素数
#   如:
#     L = prime_m2n(10, 20)
#     print(L)   [11, 13, 17, 19]

def prime_m2n(m, n):
    return [i for i in range(m, n + 1) if isprimes(i)]
    # L = []
    # for i in range(m, n + 1):
    #     if isprimes(i):
    #         L.append(i)
    # return L

L = prime_m2n(10, 20)
print(L)  # [11, 13, 17, 19]


# 4. 写一个函数primes(n)  返回指定范围内n的素数(包含n)的列表,并打印这些素数
#   L = primes(10)
#   print(L)  # [2, 3, 5, 7]
#     1) 打印100以内的全部素数
#     2) 打印200以内的全部素数

def primes(n):
    return prime_m2n(2, n)

L = primes(10)
print(L)  # [2, 3, 5, 7]
# 1) 打印100以内的全部素数
print("100以内的全部素数", primes(100))
# 2) 打印200以内的全部素数
print("200以内的全部素数", primes(200))
