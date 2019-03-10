
# 练习:
#   写一个程序，让用户输入很多正整数，当输入小于零的数时结束输入
#     1) 打印这些数的和
#     2) 打印这些数的最大数和第二大的数
#     3) 删除最小的一个数
#     4) 按原来输入的顺序打印出剩余的这些数

L = []  # 先创建一个列表，准备保存用户输入的正整数

while True:  # 循环读入这些数　存于列表L中
    s = int(input("请输入正整数: "))
    if s < 0:  # 如果用户输入的数已经是负数，结束输入
        break
    L.append(s)

# 1) 打印这些数的和
print('和是: ', sum(L))
# 2) 打印这些数的最大数和第二大的数
L2 = L.copy()
L2.sort()
print('L2=', L2)
print("最大的数是:", L2[-1])
print("第二大的数是:", L2[-2])

# 3) 删除最小的一个数
L.remove(L2[0])
# 4) 按原来输入的顺序打印出剩余的这些数
print(L)


