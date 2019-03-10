# global2.py

v = [1, 2, 3]


def fx():
    global v
    v = [4, 5, 6]


print(id(v))
fx()
print(id(v))

print('v=', v)  # [1,2,3]