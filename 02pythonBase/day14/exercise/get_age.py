# 练习:
#   写一个函数 get_age() 用来获取一个人的年龄信息
#     此函数规定用户只能输入1 ~ 140之间的数。如果用户输入其它 的数则直接触发ValueError类型的错误来通知调用来，由调用者来处理

#   def get_age():
#       ....

#   try:
#      age = get_age()
#      print('用户输入的年龄是:', age)
#   except ValueError as err:
#       print("用户输入的不是1~140之间的数")

def get_age():
    s = input("请输入年龄(1~140): ")
    a = int(s)
    if 1 <= a <= 140:
        return a
    raise ValueError('用户输入的不是1~140的整数')

try:
    age = get_age()
    print('用户输入的年龄是:', age)
except ValueError as err:
    print("用户输入的不是1~140之间的数")
