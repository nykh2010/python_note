# 练习:
#   写一个函数mymax, 实现返回两个数的最大值:
#     如:
#       def mymax(a, b):
#           ...

#     # 以下是调用:
#       print(mymax(100, 200))  # 200
#       print(mymax("ABC", "123"))  # ABC

# 方法1
def mymax(a, b):
    if a > b:
        return a
    else:
        return b


# 方法2
def mymax(a, b):
    if a > b:
        return a
    return b


# 方法3
def mymax(a, b):
    return a if a > b else b


# 方法4
def mymax(a, b):
    print("方法4的函数被执行...")
    return max(a, b)


# 以下是调用:
print(mymax(100, 200))  # 200
print(mymax("ABC", "123"))  # ABC
