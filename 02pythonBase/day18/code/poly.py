# poly.py

class Shape:
    def draw(self):
        print("正在调用Shape.draw方法")

class Point(Shape):
    def draw(self):
        print("正在调用Point.draw方法")

class Circle(Point):
    def draw(self):
        print("正在调用Circle.draw方法")

def my_draw(s):
    s.draw()  # 此处调用哪儿个方法呢?

s1 = Circle()
s2 = Point()
my_draw(s1)
my_draw(s2)