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
except ValueError:
    print("出现值错误")
else:  # 此子句只能在try内没有异常时行执行
    print("当前try语句内没有发生任何异常我才会执行")
finally:
    # 此子句中的语句无论何时，只要try语句执行，
    # finally一定会被执行
    print("我是finllay,我一定会被执行的")



print("程序正常结束")
