# mymod2.py

# 此示例示意模块内__all__列表的用法 
__all__ = ['hello1', 'name1']
# 此列表限定在其它模块用 from mymod2 import *时只导入hello1和name1
def hello1():
    pass

def hello2():
    pass

def hello3():
    pass

name1 = 'aaaa'
name2 = 'bbbb'