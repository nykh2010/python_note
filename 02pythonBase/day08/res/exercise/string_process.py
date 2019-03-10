# 练习:
#   任意输入一个字符串,将此字符串中的空格全部去除,再将此字符串返转后打印出来
#   如:
#     请输入: a bc def g<回车>
#     输出:
#        gfedcba
#        (提示: 可以用反向切片,也可以用reversed函数进行反转)

s = input("请输入: ")
# 方法1
# lst = s.split()
# s2 = ''.join(lst)
# print('s=', s)
# print("s2=", s2)
# s3 = s2[::-1]
# print("结果是: ", s3)

# 方法2
s2 = ''  # 用于保存累加结果
for x in reversed(s):
    if x != ' ':  # 如果x不是空格,就加入到s2末尾
        s2 += x
print("结果是:", s2)



