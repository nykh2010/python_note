# break4.py

i = 1
while i < 10:
    j = 0
    while j < 10:
        print(j, end=' ')
        if j == 5:
            break
        j += 1
    print()

    i += 1

print("程序结束!")