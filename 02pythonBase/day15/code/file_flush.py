# file_flush.py


# 此示例示意用F.flush来清空缓冲区
import time
f = open('myflush.txt', 'w')
# while True:
#     f.write('aaaaaaaaaa' * 40)
#     time.sleep(1)

f.write('aaaaaaaaaa')
f.flush()  # 清空缓冲区

input("请输入回车键继执行: ")
f.close()
print("程序正常退出")
