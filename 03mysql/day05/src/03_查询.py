import pymysql

# 创建数据库连接对象
db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     database="db5",
                     charset="utf8")
# 创建游标对象
cursor = db.cursor()
# 查询,查询结果都在cursor游标对象中
sel = 'select * from t1'
cursor.execute(sel)

# fetchone()
One = cursor.fetchone()
print(One)
print("*" * 30)
# fetchmany(2)
Many = cursor.fetchmany(2)
# ((2, '杜甫', 75.0), (3, '白居易', 80.0))
for each in Many:
    print(each)
print("*" * 30)
# fetchall()
All = cursor.fetchall()
for each in All:
    print(each)

cursor.close()
db.close()










