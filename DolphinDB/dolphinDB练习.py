# 此文件用于定义DolphinDB数据库的相关操作


import dolphindb as ddb

# 创建会话
s = ddb.session()

# 连接到地址为localhost，端口为8848的DolphinDB数据库，用户名为admin，密码为123456
s.connect("localhost", 8848, "admin", "123456")
print(s)

# data = s.run("SELECT * FROM firstdb.firsttb;")
# data = s.run("1..10")
# data = s.run("1..10$5:2")
# data = s.upload({"name": "yinshuai"})  # 上传数据
# data_1 = s.run("typestr(name);")  # 查看数据类型
# data_2 = s.run("name;")  # 获取数据


# data = s.loadTable(tableName="firsttb", dbPath="dfs://firstdb")  # 加载数据表数据，参数--tableName：数据表名，--dbPath：数据库路径
data = s.loadTableBySQL(tableName="firsttb", dbPath="dfs://firstdb",
                        sql="select * from firsttb")  # 加载数据表数据，参数--tableName：数据表名，--dbPath：数据库路径
# print(data)
# print(data.rows, data.cols)
# print(data.select(["id", "sym", "price", "qty"]).where("id<2").toDF())  # 对数据进行筛选
# print(data.select("*").where("id<2").toDF())

print(data.top(10).toDF())

# print(data.toDF())

print(s.run("1+1;"))
s.close()
