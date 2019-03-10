 # 2. 打印　1 ~ 20 的整数，每行打印5个，打印４行
 #    1 2 3 4 5
 #    6 7 8 9 10
 #    11 12 13 14 15


# 方法1
# i = 1
# while i <= 20:
#     # 打印i对应的数,不换行
#     print(i, end=' ')
#     if i == 5:
#         print()
#     elif i == 10:
#         print()
#     elif i == 15:
#         print()
#     elif i == 20:
#         print()
#     # 将i绑定的数值变化一下
#     i += 1

# # 方法2
# i = 1
# while i <= 20:
#     # 打印i对应的数,不换行
#     print(i, end=' ')
#     if i % 5 == 0:
#         print()  # 换行
#     # 将i绑定的数值变化一下
#     i += 1


# 方法3
i = 1
while i <= 20:
    # 打印i对应的数,不换行
    print(i, end=' ')
    i += 1

    if (i - 1) % 5 == 0:
        print()  # 换行
    # 将i绑定的数值变化一下
