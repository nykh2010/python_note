# 练习:
#   １．任意输入一段字符串:
#     1) 计算出您输入的字符串中的'a' 这个字符的个数，并打印个数
#     如:
#       请输入: abcd abc bc a
# 　　　　输出:
#       您输入的a的个数是: 3
#     (要求，不允许使用S.count方法)

s = input('请输入: ')
count = 0  # 初始化一个变量用于计数
for ch in s:
    if ch == 'a':
        count += 1
else:
    print("您输入的a的个数是:", count)










    
