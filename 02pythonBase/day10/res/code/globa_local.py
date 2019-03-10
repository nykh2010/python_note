# globa_local.py


# 此示例说明局部变量和全局变量

a = 100  # a,b为全局变量
b = 200
def fx(c):
    d = 400  # c,d为局部变量
    b = 20000  # 
    print(a, b, c, d)

fx(300)
print('a=', a)
print('b=', b)
# print('c=', c)  # 出错


