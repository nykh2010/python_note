# 练习:
#   写一个函数 mysum, 可以传入任意个实参的数字,
#   此函数返回所有实参的和:
#   def mysum(*args):
#       ...  # <<<--- 此处需要自己实现

#   print(mysum(1, 2, 3, 4))  # 10
#   print(mysum(1, 2, 3, 4, 5))  # 15

def mysum(*args):
    print("第11行的mysum被调用!")
    s = 0  # 用于累加和
    for x in args:
        s += x
    return s

def mysum(*args):
    print("第17行的mysum被调用!")
    return sum(args)


print(mysum(1, 2, 3, 4))  # 10
print(mysum(1, 2, 3, 4, 5))  # 15


