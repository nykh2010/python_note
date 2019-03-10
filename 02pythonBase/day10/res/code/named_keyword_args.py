# named_keyword_args.py


# 此示例示意命名关键字形参的用法:

def f1(*, b, c):
    print("b=", b)
    print("c=", c)

f1(c=2, b=1)  # 错误

def f2(a, b, *args, c, d):
    print('f2.a=', a)
    print('f2.b=', b)
    print('f2.args=', args)
    print('f2.c=', c)
    print('f2.d=', d)

f2(1, 2, 3, 4, c=5, d=6)
d = {'d': 44, 'c': 33}
f2(11, 22, **d)  # f2(11, 22, c=33, d=44)



