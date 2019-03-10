# file_read.py

# 此示例示意文件的打开及读取文件数据

try:
    f = open("myfile.txt")  # f将绑定文件流对象
    print("打开文件成功")

    # ...　此处代码可以对myfile.txt进行读操作
    L = f.readlines()
    print(L)

    f.close()
    print("文件已成功关闭")
except OSError:
    print("打开文件失败")