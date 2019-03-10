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
    print("苹果不分了")
except:
    print("除ValueError类型之前的错误被捕获并处理")

# except ValueError:
#     print("苹果不分了")
# except ZeroDivisionError:
#     print("苹果不分了")


print("程序正常结束")
