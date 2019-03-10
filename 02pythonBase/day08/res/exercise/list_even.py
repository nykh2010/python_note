# 练习:
#   输入一个开始的整数用begin绑定
#   输入一个结束的整数用end绑定
#   将从begin开始，到end结束范围(不包含end)的所有的偶数存于列表中,并打印
#   (建议用列表推导式完成)

begin = int(input("请输入开始数: "))
end = int(input("请输入结束数: "))

L = [x for x in range(begin, end) if x % 2 == 0]
print(L)

