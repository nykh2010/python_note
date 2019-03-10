# assert.py

# 此示例示意assert语句的用法 
def get_age():
    a = input("请输入年龄: ")
    a = int(a)
    assert 1 <= a <= 140, '年龄不在有效范围内'
    return a

try:
    age = get_age()
    print(age)
except AssertionError as err:
    print(err)

    