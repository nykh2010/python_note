from mysqlpy import Mysqlpy

sqlh = Mysqlpy('db5')
name = input("请输入姓名:")
# score = input("请输入成绩:")
# ins = 'insert into t1(name,score) values(%s,%s)'
# sqlh.zhixing(ins,[name,score])

sel = 'select * from t1 where name=%s'
result = sqlh.all(sel,[name])
print(result)