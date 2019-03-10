# file_write_text.py


# 此示例示意文本文件的写操作
# f = open("mynote.txt", 'w')  # 'w' 代表写write操作
# f = open("mynote.txt", 'x')  # 如果文件已存在,则报错
f = open("mynote.txt", 'a')  # 'a' 代表append追加
print("打开文件成功")

f.writelines(['abcd', '1234'])
f.write("你好!aaaaaaa")

print("写文件成功")

f.close()
print("已关闭文件")







