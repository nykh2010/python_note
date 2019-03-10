# 6. 输入一个整数，按宽度打印如下矩形:
#   请输入: 5
#       1 2 3 4 5
#       2 3 4 5 6
#       3 4 5 6 7
#       4 5 6 7 8
#       5 6 7 8 9
#   请输入: 3
#       1 2 3
#       2 3 4
#       3 4 5

w = int(input('请输入正方形的宽度: '))
for line in range(1, w + 1):
    for i in range(line, line+w):
        print(i, end=' ')
    print()  # 换行



