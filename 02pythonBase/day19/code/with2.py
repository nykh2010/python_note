# with.py

# 此示例示意用with语句绑定文件对象
try:
    with open('../day19.txt','r') as f:
    # 以下程序统计day19.txt中有多少个字
        count = 0
        for line in f:
            count += len(line)
            # 3 / 0  # 故意制造一个错误
        print("字个数是:", count)
except OSError:
    print("文件没有打开")
except ZeroDivisionError:
    print("操作文件时有错")

