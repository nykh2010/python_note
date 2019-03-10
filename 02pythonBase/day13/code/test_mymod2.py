# test_mymod.py


# 此示例示意不同模块内可以有同名的全局变量，不会冲突
import mymod  # 导入自定义模块

name1 = "我的名字1"
print(name1)  # 我的名字1
print(mymod.name1)  # BYD
