# 练习:
#   有一个集合:
#     s = {'Tom', 'Jerry', 'Spike', 'Tyke'}
#     用for语句实现遍历如下:
#     for x in s:
#         print(x)
#     else:
#         print('遍历结束')
#     请将上面的for语句改写为while语句和迭代器实现


s = {'Tom', 'Jerry', 'Spike', 'Tyke'}
for x in s:
    print(x)
else:
    print('遍历结束')
  
it = iter(s)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print('遍历结束')
        break