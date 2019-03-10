# 练习:
#   1. 写程序,实现复制文件功能(只复制文件,不复制文件夹)
#     要求:
#       1. 源文件名和目标文件名需手动输入
#       2. 要考虑文件关闭问题
#       3. 要考虑超大文件问题
#       4. 要能复制二进制文件

src_file = input("请输入源文件名: ")
dst_file = input("请输入目标文件名: ")
try:
    with open(src_file, 'rb') as fr, open(dst_file, 'wb') as fw:
        # 解决大文件问题:
        while True:
            b = fr.read(4096)
            if not b:
                break
            fw.write(b)
except OSError:
    print('复制失败')



