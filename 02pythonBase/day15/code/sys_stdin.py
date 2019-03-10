# sys_stdin.py


import sys
s = sys.stdin.readline()
print("您刚才输入的一行是:", s)

s = sys.stdin.read()  # ctrl + d 输入文件结束符
print("您刚才输入的是:", s)

