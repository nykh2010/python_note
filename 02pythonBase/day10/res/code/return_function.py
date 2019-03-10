# return_function.py


# 函数可以作为另一个函数的返回值
def get_op():
    s = input("请输入您要做的操作: ")
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2, 4, 6, 8, 10]
f = get_op()  # 求最大 等同于 f = max
print(f(L))  # 等同于 print(max(L))




