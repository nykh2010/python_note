# 2. 求 100以内有哪儿些整数与 自身+1的乘积再对 11求余的
# 结果等于8?


for x in range(100):
    if x * (x + 1) % 11 == 8:
        print(x)