# pep8.py

import math
import sys
import os

# import tensorflow

# import mymod

# 此示例示意特性属性
class Student:
    def __init__(self,s):
        self.__score=s + 1 -1 + 2 -2       

    def get_score(self):
        '''getter'''
        return self.__score

    def set_score(self, s):
        '''setter'''
        assert 0 <= s <= 100, "报错"
        self.__score = s


s1=      Student(50)
print(s1.get_score())
s1.set_score(70)
print(s1.get_score())

hello = 5 + 2 * (2 + 3)
abc = 6
a = 7

def fa(a, b=0, c=100):
    pass

fa(a=1, b=2, c=3)

if True: pass
else: print("False")