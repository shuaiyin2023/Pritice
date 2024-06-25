import datetime
import pymysql  # 此处pymysql报错是因为同时安装了其他数据库连接器mysql-connector，导致冲突，如果想继续使用，将其中一个卸载即可

from djangoProject.settings import DATABASE_PASSWORD, DATABASE_USER, DATABASE_NAME

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user=DATABASE_USER,
                     password=DATABASE_PASSWORD,
                     database=DATABASE_NAME,
                     cursorclass=pymysql.cursors.DictCursor  # 设置以字典格式返回结果，默认为元组
                     )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# sql = "select * from app01_StudentInfo"
# 获取当前日期时间并转换为SQL日期时间格式
# current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# sql = ("insert into app01_StudentInfo (name, sex, profession, email, qq, phone, status, created_time) values "
#        "('liangzai', 2, 'moyu', '2113131@qq.com', 122121, 1313434, 1, '%s')") % current_time

sql_2 = "select * from app01_StudentInfo"

cursor.execute(sql_2)
data = cursor.fetchall()
# data = cursor.fetchone()
print(data)
# print(len(data))
print("==========================================\n")

update_sql = "update app01_StudentInfo set name='机器人' where id = 6"
cursor.execute(update_sql)
db.commit()
print("==========================================\n")


cursor.execute(sql_2)
data = cursor.fetchall()
print(data)
print(len(data))
print("==========================================\n")

db.close()




