# file_write_binary.py


b = bytes(range(256))  # 生成256个字节

try:
    f = open('mybinary.bin', 'wb')
    f.write(b)  # 写入256个字节
    f.close()
    print("写入成功")
except OSError:
    print("打开二进制写文件出错")



