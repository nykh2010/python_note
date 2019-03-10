import pymysql

# 创建数据库连接对象
db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     database="db5",
                     charset="utf8",
                     port=3306)
# 利用连接对象创建对象
cursor = db.cursor()
# 利用游标对象的execute()方法执行sql命令
cursor.execute('insert into t1(name,score) \
                values("陶渊明",88)')

cursor.execute('insert into t1(name,score) \
                values("小姐姐",100)')

#　提交到数据库执行
db.commit()
print("ok")
# 关闭游标
cursor.close()
# 断开连接
db.close()














