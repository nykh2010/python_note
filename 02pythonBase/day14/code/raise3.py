# raise.py

# 此示例示意用raise语句发出异常通知并进入异常状态
def make_except():
    print("开始...")
    # raise ValueError  # 触发ValueError类型的错误，进入异常状态
    # err = ValueError("这是我故意制造的一个错误，看谁能捕获")
    # raise err
    raise ZeroDivisionError("其实没有被零除，逗泥湾")
    print("结束.")


try:
    make_except()
except ValueError as e:
    print("收到错误通知，并转为正常状态")
    print("错误信息是:", e)

print("程序正常结束")

