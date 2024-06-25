import mysql.connector

from djangoProject.settings import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER

db = mysql.connector.connect(host='localhost',
                             user=DATABASE_USER,
                             password=DATABASE_PASSWORD,
                             database=DATABASE_NAME,
                             # 此参数是因为mysql8.0及之后的版本使用的密码验证方式是caching_sha2_password，而此连接器不支持此认证方式，
                             # 所以需要指定认证方式为 mysql_native_password
                             auth_plugin='mysql_native_password'
                             )

# 创建游标
cursor = db.cursor(dictionary=True)  # mysql-connector设置返回数据的格式在创建游标对象时

sql = "select * from app01_student"
cursor.execute(sql)
data = cursor.fetchall()
print(data)
print("插入之前一共有{}条数据".format(len(data)))
print("=========================分割线=========================\n")

insert_sql = "insert into app01_student(name, age) values (%s, %s)"
value = [("John", 25), ("Smith", 21), ("Jane", 23)]
cursor.executemany(insert_sql, value)
db.commit()
print("插入成功")
print("=========================分割线=========================\n")

cursor.execute(sql)
data = cursor.fetchall()
print(data)
print("插入之后一共有{}条数据".format(len(data)))

db.close()
