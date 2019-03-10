# 2. 写一个程序，任意输入一些数存于列表L中，当输入负数时 
#     结束输入
# 　　1) 将列表中数字存入到另一个列表L2中，要求:
#      重复输出多次的数字只在L2中保留一份(去重)
#      如:
#        L = [1, 3, 2, 1, 6, 4, 2, .... 98, 82]
#        则:
#        L2 = [1, 3, 2, 6, 4, 98, 82]

L = []
while True:
    n = int(input("请输入正整数: "))
    if n < 0:
        break
    L.append(n)

print('L=', L)

L2 = []  # 先创建一个列表准备放入
# for x in L:  # 遍历L列表中的所有元素
#     # 判断x已经存在于列表L2中
#     if x in L2:
#         pass  # continue
#     else:  # 如果不存在,则放入L2中
#         L2.append(x)

for x in L:  # 遍历L列表中的所有元素
    # 判断x已经存在于列表L2中
    if x not in L2:
        L2.append(x)

print(L2)



