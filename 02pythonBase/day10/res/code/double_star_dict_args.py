# double_star_dict_args.py


# 此示例示意双星号字典形参的用法
def f1(**kwargs):
    print("参数个数是:", len(kwargs))
    print('kwargs =', kwargs)

f1(a=1, b=2, c=3)

d = {'d':44, 'e':55}

f1(a=1, b=2, c=3, **d)