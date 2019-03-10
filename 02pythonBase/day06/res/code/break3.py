# break.py


i = 1

while i <= 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("while 的else 子句部分被执行!")

print('i=', i)  # i = 7