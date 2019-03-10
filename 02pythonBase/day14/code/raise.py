# raise.py

# 此示例示意用raise语句发出异常通知并进入异常状态
def make_except():
    print("开始...")
    raise ValueError  # 触发ValueError类型的错误，进入异常状态
    print("结束.")


try:
    make_except()
except ValueError:
    print("收到错误通知，并转为正常状态")

print("程序正常结束")

