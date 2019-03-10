# 输入字符串，打印字符串的第一个数据，中间的数据，
# 最后的数据。如果输入的字符串长度是偶数，
# 中间数据不输出。
s = input("请输入数据")
if s == "":
    print("什么都没有输入")
    quit()#退出程序
#第一个数据
print(s[0])#正向索引
print(s[-len(s)])#反向索引
#最后一个数据
print(s[len(s)-1])
print(s[-1])

if len(s)%2 ==1:
    #len(s)//2  7//2=3
    print(s[len(s)//2])
else:
    print("没有中间数据")
