# 1. 写一个函数 get_score() 来获取用户输入的学生成绩(0~100)整数
# 如果用户输入出现异常，则此函数返回0,否则近观回用户输入的成绩，同时保存这个成绩一定在0~100之间
# def get_score():
#     ....

# score = get_score()
# print("学生的成绩是:", score)


def get_score():
    s = input('请输入学生成绩: ')
    try:
        s = int(s)
    except:
        return 0
    if 0 <= s <= 100:
        return s
    return 0

score = get_score()
print("学生的成绩是:", score)
