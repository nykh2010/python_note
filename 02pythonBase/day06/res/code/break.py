# break.py


i = 1

while i <= 6:
    print("循环开始时: i=", i)
    if i == 3:
        break

    print("循环结束时: i=", i)
    i += 1


print('i=', i)  # i = 7