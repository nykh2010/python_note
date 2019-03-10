# 练习:
#   经理有: 曹操, 刘备, 孙权
#   技术员有: 曹操, 孙权, 张飞, 关羽
#   用集合求:
#     1. 即是经理也是技术员的有谁?
#     2. 是经理,但不是技术人员的有谁?
#     3. 是技术人员,不是经理的都有谁?
#     4. 张飞是经理吗?
#     5. 身兼一职的人都有谁?
#     6. 经理和技术员共有几个人?


mananger = {'曹操', '刘备', '孙权'}
tech = {'曹操', '孙权', '张飞', '关羽'}

print("即是经理也是技术员的有", mananger & tech)
print("是经理,但不是技术人员的有", mananger - tech)
print("是技术人员,不是经理的都有", tech - mananger)
if '张飞' in tech:
    print("张飞是经理")
else:
    print("张飞不是经理")
print("身兼一职的人都有", mananger ^ tech)
print("经理和技术员共有%d个人" % len(mananger | tech))
