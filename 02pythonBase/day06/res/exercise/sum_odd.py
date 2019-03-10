# 3. 计算 1 + 3 + 5 + 7 + .... + 99 的和并打印出来
#   要求:
#     1. 用for 语句实现
#     2. 用while 语句实现


# 1. 用for 语句实现
s = 0
for i in range(1, 100, 2):
    s += i
print("和是:", s)

# 2. 用while 语句实现
s = 0
i = 1
while i < 100:
    # 求和
    s += i
    i += 2
print("和是:", s)

