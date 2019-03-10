import pymysql

class Mysqlpy:
    def __init__(self,database,host="localhost",
                               user="root",
                               password="123456",
                               charset="utf8",
                               port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port

    def open(self):
        self.db = pymysql.connect(host=self.host,
                          user=self.user,
                          password=self.password,
                          database=self.database,
                          charset=self.charset,
                          port=self.port)
        self.cursor = self.db.cursor()


    def close(self):
        self.cursor.close()
        self.db.close()

    def zhixing(self,sql,L=[]):
        self.open()
        self.cursor.execute(sql,L)
        self.db.commit()
        self.close()


    def all(self,sql,L=[]):
        self.open()
        self.cursor.execute(sql,L)
        result = self.cursor.fetchall()
        self.close()

        return result


if __name__ == "__main__":
    sqlh = Mysqlpy('db5')
    name = input("请输入姓名:")
    # score = input("请输入成绩:")
    # ins = 'insert into t1(name,score) values(%s,%s)'
    # sqlh.zhixing(ins,[name,score])

    sel = 'select * from t1 where name=%s'
    result = sqlh.all(sel,[name])
    print(result)

















