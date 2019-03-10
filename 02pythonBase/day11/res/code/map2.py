# map.py


def mypow_x_y(x, y):
    return x ** y


# 用map函数生成一个可迭代对象,此可迭代对象可以生成:
#    1 ** 4, 2 ** 3, 3 ** 2, 4 ** 1
for x in map(mypow_x_y, range(1, 5), range(4, 0, -1)):
    print(x)  # 1, 8, 9, 4


print(sum(map(pow, range(1, 5), range(4, 0, -1))))

for x in map(pow, [1, 2, 3, 4], [5, 6], range(5, 100)):
    print(x)

