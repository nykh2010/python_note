# 定义一个"人" Human 类
#    class Human:
#        def set_info(self, name, age, address='不详'):
#        　　　...此方法用来给人对象添加姓名,年龄，家庭住址属性

#        def show_info(self):
#            ... 此处显示此人的信息
#    如:
#      s1 = Human()
#      s1.set_info("小张", 20, '北京市朝阳区')
#      s2 = Human()
#      s2.set_info('小李', 18)
#      s1.show_info()  # 小张　今年　20　岁，　家庭住址:　北京市朝阳区　
#      s1.show_info()  # 小李 今年 18　岁，　家庭住址:　不详



class Human:
    def set_info(self, name, age, address='不详'):
        '''此方法用来给人对象添加姓名,年龄，家庭住址属性'''
        self.name = name
        self.age = age
        self.address = address

    def show_info(self):
        '''此处显示此人的信息'''
        print(self.name, '今年',
              self.age, '岁,家庭住址:',
              self.address)

s1 = Human()
s1.set_info("小张", 20, '北京市朝阳区')
s2 = Human()
s2.set_info('小李', 18)
s1.show_info()  # 小张　今年　20　岁，　家庭住址:　北京市朝阳区　
s2.show_info()  # 小李 今年 18　岁，　家庭住址:　不详
