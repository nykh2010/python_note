# 练习:
#   已知有列表:
#     L = [3, 5]
#     用索引和切片操作，将原列表改变为:
#     L = [1, 2, 3, 4, 5, 6]
#     将列表反转,删除最后一个元素后打印此列表:
#     ...
#     print(L)  # [6, 5, 4, 3, 2]

L = [3, 5]
L[1:1] = [4]
L[0:0] = [1, 2]
L[len(L):] = [6]
print(L)  # L = [1, 2, 3, 4, 5, 6]
# 将列表反转,删除最后一个元素后打印此列表:
L[:] = L[::-1]
del L[-1]
print(L)  # [6, 5, 4, 3, 2]
