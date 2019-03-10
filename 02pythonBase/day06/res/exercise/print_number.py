# 　　1. 写程序，输入一个开始整数用变量begin绑定
# 　　输入一个结束的整数用变量end 绑定
#   打印从begin开始到end(不包含end结束)的每个整数，
#   打印在一行内
#   请输入开始值: 8
#   请输入结束值: 20
#   8 9 10 11 .... 19 20

begin = int(input("请输入开始值: "))
end = int(input("请输入结束值: "))

i = begin
while i < end:
    print(i, end=' ')
    i += 1

print()  # 换行


print('---------以下是5个数字打印在一行--------')

# 方法1
# i = begin
# while i < end:
#     print(i, end=' ')
#     # 什么时候开始打印这个换行

#     if (i - begin) % 5 == 4:
#         print()

#     i += 1

# print()  # 换行

# 方法2  用一个专用的变量来记录个数:
i = begin
count = 0  # 用来记录已经打印的数的个数　
while i < end:
    print(i, end=' ')
    count += 1  # 已经在终端打印过，所以个数要加1
    if count % 5 == 0:  # 计够5个就打印一次换行　
        print()

    i += 1

print()  # 换行

