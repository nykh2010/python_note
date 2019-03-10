# attribute.py

class Dog:
    def eat(self, food):
        print(self.color, '的', self.kinds,
              '正在吃', food)
        self.last_food = food  #　记住上次吃的是什么？


dog1 = Dog()
dog1.kinds = "京巴"  # 添加属性kinds
dog1.color = "白色"  # 添加属性color
dog1.color = "黄色"  # 修改属性color
print(dog1.color, '的', dog1.kinds)  # 黄色的京巴

dog2 = Dog()
dog2.color = "黑色"
dog2.kinds = '导盲犬'
print(dog2.color, "的", dog2.kinds)  # 出错

dog1.eat("包子")  # 黄色 的 京巴 正在吃 包子
dog2.eat('狗粮')  # 黑色 的 导盲犬 正在吃 狗粮

print(dog1.last_food)  # 包子
print(dog2.last_food)  # 狗粮

