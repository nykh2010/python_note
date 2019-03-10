# 练习:
#   用递归实现求阶乘的函数 myfac(x)
#     def myfac(x):
#          ...

#     print(myfac(5))  # 120
#     print(myfac(4))  # 24
# 5! = 5 * 4!
# 5! = 5 * 4 * 3!
# 5! = 5 * 4 * 3 * 2!
# 5! = 5 * 4 * 3 * 2 * 1!
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 5 * 24
# 5! = 120

def myfac(x):
    # 我只知道1!是1 
    if x == 1:
        return 1
    return x * myfac(x - 1)

print(myfac(5))  # 120
print(myfac(4))  # 24