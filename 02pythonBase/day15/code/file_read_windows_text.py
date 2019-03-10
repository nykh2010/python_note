# file_read.py

# 此示例示意文件的打开及读取文件数据

try:
    f = open("myfile_windows.txt")
    print("打开文件成功")

    s = f.read()
    print("您读取到%d个字符" % len(s))


    f.close()
    print("文件已成功关闭")
except OSError:
    print("打开文件失败")