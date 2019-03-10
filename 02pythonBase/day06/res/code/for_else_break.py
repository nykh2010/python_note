# for_else.py


#　此示例示意else子句的用法:
# 2.  当在循环语句内部用break终止循环时，else子句部分
#   的语句不会执行
s = 'ABCD'
for c in s:
    print(c)  # A B
    if c == 'B':
        break
else:
    print("for 语句的else子句被执行")


print("程序结束")