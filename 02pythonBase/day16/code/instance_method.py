# instance_method.py


# 此示例示意实例方法的定义和调用
class Dog:
    def eat(self, food):
        print("id为", id(self), '的小狗正在吃:', food)

    def sleep(self, hour):
        print("id为", id(self), '的小狗睡了', hour, '小时')

    def play(self, obj):
        print("id为", id(self), '的小狗正在玩', obj)

dog1 = Dog()
dog1.eat('骨头')

dog2 = Dog()
dog2.eat("狗粮")

dog1.sleep(1)  # id为xxxx.的小狗睡了 1 小时
dog2.sleep(2)  # id为yyyy.的小狗睡了 2 小时
dog1.play('球')  # id为xxxx.的小狗正在玩 球
dog2.play('飞盘')  # id为yyyy.的小狗正在玩 飞盘


