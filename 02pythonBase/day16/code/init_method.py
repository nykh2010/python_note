# init_method.py


class Car:
    def __init__(self, c, b, m):
        self.color = c  # 颜色
        self.brand = b  # 品牌
        self.model = m  # 型号
        return None
        print("__init__方法被调用")

    def run(self, speed):
        print(self.color, '的', self.brand,
              self.model, '正在以', speed,
              '公里/小时的速度行驶')

    def change_color(self, clr):
        '''换颜色'''
        self.color = clr


a4 = Car("红色", "奥迪", "A4")
a4.run(280)
a4.change_color("黑色")
a4.run(300)

t1 = Car("蓝色", "TESLA", "Model S")
t1.run(270)











