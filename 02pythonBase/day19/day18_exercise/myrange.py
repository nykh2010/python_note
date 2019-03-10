
# 实现自定义的MyRange类

class MyRange:
    def __init__(self, start,
                 stop=None,
                 step=None):
        if step is None:
            step = 1
        if stop is None:
            stop = start
            start = 0
        # 以下是为了保存数据
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return MyRange_iter(self.start,
                            self.stop,
                            self.step)

class MyRange_iter:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step  # 假设step一直大于

    def __next__(self):
        if self.step > 0:  # 正向生成
            if self.start >= self.stop:
                raise StopIteration
            r = self.start
            self.start += self.step
            return r

for x in MyRange(4):
    print(x)  # 0 1 2 3

print('==========')
for y in MyRange(4, 6):
    print(y)  # 4, 5

z = [x for x in MyRange(1, 10, 3)]  # z=[1, 4, 7]
print('z=', z)
