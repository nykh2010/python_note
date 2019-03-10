# filter.py


# 判断x是否为奇数,如果是奇数返回True,否则返回False
def isodd(x):
    if x % 2 == 1:
        return True
    return False


# 打印1~10以内的所有奇数:
for x in filter(isodd, range(10)):
    print(x)

L = [1, 8, 5, 3, 23, 1, 3, 5, 7, 8]
L2 = list(filter(isodd, L))
print(L2)


