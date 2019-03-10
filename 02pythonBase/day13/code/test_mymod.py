# test_mymod.py


print("------第一种导入方式-----")
import mymod  # 导入自定义模块

mymod.mysum(100)
mymod.myfac(5)
print(mymod.name1)

print("------第二种导入方式-----")
from mymod import name2
print(name2)

print("------第三种导入方式-----")
from mymod import *
myfac(10)
mysum(1000)

