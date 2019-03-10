# try_finally.py

# 此示例示意try_finally的用法和作用
def fry_egg():
    try:
        print("打开天燃气....")
        try:
            count = int(input('请输入鸡蛋个数: '))
            print("完成了煎鸡蛋， 共煎了%d个鸡蛋" % count)
        finally:
            print("关闭天燃气")
    except ValueError:
        print("出现了值错误,已转为正常状态")


fry_egg()

print("程序正常结束")