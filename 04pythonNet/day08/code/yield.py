# yield.py

def mynumber(n):
    i = 1
    while i < n:
        print("即将生成:", i)
        yield i
        i += 1
    print("生成器函数终止")

def task2():
    for x in mynumber(5):
        print('x=', x)

task2()

# it = iter(mynumber(4))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  # StopIteration