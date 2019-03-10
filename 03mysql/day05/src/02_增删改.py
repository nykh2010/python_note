import pymysql

# 创建数据库连接对象
db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     database="db5",
                     charset="utf8")
# 创建游标对象
cursor = db.cursor()

try:
    # 增加
    ins = 'insert into t1(name,score) values \
           ("小妹妹",98)'
    cursor.execute(ins)
    # 修改
    upd = 'update t1 set score=100 where name="李白"'
    cursor.execute(upd)
    # 删除
    dele = 'delete from t1 where name="陶渊明"'
    cursor.execute(dele)
    # 提交到数据库执行
    db.commit()
    print("ok")
except Exception as e:
    db.rollback()
    print("Failed",e)

# 关闭游标
cursor.close()
# 断开数据库连接
db.close()











