# iterator1.py

L = [2, 3, 5, 7]

# 用for循环访问可迭代对象
# for x in L:
#     print(x)

it = iter(L)  # 先拿到迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break




