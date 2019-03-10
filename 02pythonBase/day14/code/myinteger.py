# myinteger.py

def myinteger(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in myinteger(100000000000000000000000):
    if x == 3:
        break
    print(x)  # 打印 0, 1, 2
