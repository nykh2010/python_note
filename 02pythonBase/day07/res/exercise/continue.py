# １．　求 1 ~ 500 之间(不包含500)所有 不能被 5或 7或 11 整除的数的和
#   　求：
#   　　　　1 + 2 + 3 + 4 + 6 + 8 + 9 + 12 + .... 的和


s = 0  # 用于累加结果
# for x in range(500):
#     if x % 5 == 0:
#         continue

#     if x % 7 == 0:
#         continue

#     if x % 11 == 0:
#         continue
#     s += x



for x in range(500):
    if x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        continue

    s += x

print(s)