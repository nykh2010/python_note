# mymod3.py

# 此示例示意 隐藏属性在from mymod3 import *时不会被导入
def fa():
    pass

def _fa():
    pass

def __fa():
    pass

name1 = 'aaaa'
_name1 = 'bbbb'