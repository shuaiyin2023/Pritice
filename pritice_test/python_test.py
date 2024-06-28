# 此文件用于python的各种题目练习

import json

file_path = f"D:\Company-yin\Files\info.txt"

file_list = []
with open(file_path, "r", encoding="utf-8") as f:
    content = f.readlines()

for line in content:
    first_split = line.split("\n")
    second_split = first_split[0].split(" ")

    file_list.append(
        {"name": second_split[0],
         "gender": second_split[1],
         "age": second_split[2],
         "salary": second_split[3]
         }
    )

max_salary = file_list[0]
youngest = file_list[0]
for data in file_list:
    if data["salary"] > max_salary["salary"]:
        max_salary = data

    if youngest["age"] > data["age"]:
        youngest = data

    data["name"] = data["name"].upper()

    # 过滤掉所有姓名以A和a开头的
    if data["name"].startswith("a") or data["name"].startswith("A"):
        continue
    print(data)


print("薪资最高的人的信息: ", max_salary)
print("最年轻的人的信息: ", youngest)
print("将所有姓名转为大写的数据: ", file_list)
