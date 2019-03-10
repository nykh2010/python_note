# file_read_binary.py

# 此示例示意以二进制方式读取文件内容
f = open('myfile_windows.txt', 'rb')  # r:read, b:binary
b = f.read()  # 读取全部内容
print("读取的内容是:", b)
print("读取的字节个数是: ", len(b))

s = b.decode()  # 解码为字符串
print("文件中字符的个数是:", len(s))  # 9

f.close()


