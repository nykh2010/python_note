# 练习:
#   写一个程序,从键盘输入一段字符串,用变量s绑定
#   1,将此字符串转为字节串用变量b绑定,并打印出来
#   2. 打印字符串s 的长度和字节串b的长度(用len函数)
#   3. 将b字节串再转换为字符串用变量s2绑定,判断s2与s是否相同

s = input("请输入字符串:")
# b = bytearray(s, 'utf-8')
# b = s.encode()
b = bytes(s, 'utf-8')
print("字符串长:", len(s))
print("字节串长:", len(b), '内容:', b)
s2 = b.decode()
if s == s2:
    print("s 等同于 s2")
