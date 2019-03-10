# 1. 已知有五位朋友在一起
#   第五位个人比第四个人大2岁
#   第四位个人比第三个人大2岁
#   第三位个人比第二个人大2岁
#   第二位个人比第一个人大2岁
#   第一个人说他10岁


# 1) 编写程序算出第5个人几岁
# 2) 第3个人几岁

def get_age(n):
    if n == 1:
        return 10
    return get_age(n - 1) + 2


print("第5个人:", get_age(5))
print("第3个人:", get_age(3))

