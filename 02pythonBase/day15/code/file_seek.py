# file_seek.py

# 此示例示意文件的读位置的重新定位
f = open('mydata.txt', 'rb')
f.read(2)
print("当前的读写位置是:", f.tell())
# 想读取第5个字节处的 b'abcde'

# 从文件头开始偏移
# f.seek(5, 0)
# 从当前位置开始偏移
# f.seek(3, 1)
# 从文件尾开始偏移
f.seek(-15, 2)

print("偏移后当前的位置是", f.tell())
s = f.read(5)
print(s)

f.close()


