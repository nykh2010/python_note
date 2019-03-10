# global.py

v = 100


def fx():
    global v  # 全局声明
    v = 200


fx()
print('v=', v)  # 200