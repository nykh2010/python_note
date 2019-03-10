
# 练习:
#   创建一个全局变量
#     L = []
#   写一个函数:
#     def input_number():
#         .... # <<-- 此函数内从键盘读入一个数字

#   此函数每次调用将会从键盘读入一些数据，想办法将读入的数据追加到L列表中...


L = []
def input_number():
    while True:
        s = input("请输入:")
        if s == '':
            break
        n = int(s)
        L.append(n)

input_number()

print(L)  # 打印

