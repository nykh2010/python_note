# myenum.py

def myenum(iterable, start=0):
    it = iter(iterable)
    while True:
        try:
            x = next(it)
            yield (start, x)
            start += 1
        except StopIteration:
            break


names = ['中国移动', '中国电信', '中国联通']
for t in myenum(names):
    print(t)

for t in myenum(names, 101):
    print(t)
