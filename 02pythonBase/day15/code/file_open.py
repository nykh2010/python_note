# file_open.py

# 此示例示意文件的打开和关闭，及文件打开失败的处理

try:
    f = open("myfile.txt")  # f将绑定文件流对象
    # f = open("aaaaaaa.txt")  # 文件打开失败会触发OSError异常
    print("打开文件成功")

    # ...　此处代码可以对myfile.txt进行读操作

    f.close()
    print("文件已成功关闭")
except OSError:
    print("打开文件失败")