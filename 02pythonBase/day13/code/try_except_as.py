# except1.py


# 此示例示意发生错误时程序的异常状态的处理和捕获
def div_apple(n):
    print('现在有%d个苹果，你想分给几个人?' % n)
    s = input("请输入人数: ")
    cnt = int(s)  # <<--- 此处可能会触发ValueError类型错误
    result = n / cnt  # <<-- 此外可能会触发ZeroDivisionError错误
    print("每个人分了", result, '个苹果')


try:
    div_apple(10)
    print("分苹果成功")
except ValueError as err:  # err用来绑定错误数据
    print("已有值错误发生，并已经处理且转为正常状态")
    print('错误数据是:', err)
except ZeroDivisionError:
    print("发生了被零除的错误，程序已经转为正常状态")
    print('没分苹果，苹果被收回')


print("程序正常结束")
