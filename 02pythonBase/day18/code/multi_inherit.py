# multi_inherit.py

# 此示例示意多继承

class Car:
    def run(self, speed):
        print("汽车以", speed, 'km/h的速度行驶')

class Plane:
    def fly(self, height):
        print("飞机以", height, '米的高度飞行')

class PlaneCar(Car, Plane):
    '''PlaneCar同时继承自Car,和 Plane)'''

p1 = PlaneCar()
p1.fly(10000)
p1.run(300)

