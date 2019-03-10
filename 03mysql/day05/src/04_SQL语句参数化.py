'''
请输入学生姓名:
请输入学生成绩:
ok
'''
import pymysql

# 创建数据库连接对象
db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     charset="utf8")
# 创建游标对象
cursor = db.cursor()
cursor.execute('use db5')
# 接收用户从终端输入
name = input("请输入诗人姓名:")
score = input("请输入诗人成绩:")

try:
    # 写法1(推荐)
    # %s后面不用　% () 去补位
    ins = 'insert into t1(name,score) values(%s,%s)'
    # execute第二个参数一定要为列表
    cursor.execute(ins,[name,score])
    # # 写法2(不推荐)
    # ins = "insert into t1(name,score) values('%s','%s')" \
    #                                   % (name,score)
    # cursor.execute(ins)

    db.commit()
    print("ok")
except:
    db.rollback()
    print("Failed")

cursor.close()
db.close()













