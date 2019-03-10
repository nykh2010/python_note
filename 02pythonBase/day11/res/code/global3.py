# global2.py

v = 100


def fx(v):
    global v  # 出错
    v = 300


fx(200)

print('v=', v)  # 