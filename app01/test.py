import asyncio
import random
import pandas as pd
import numpy as np

# 模拟10万条数据
# data = [{"id": i, "name": f"数据{i}"} for i in range(1, 100001)]


# 定义数据量
num_rows = 100000

# 生成随机数据
data = {
    'column1': np.random.randint(0, 100, size=num_rows),
    'column2': np.random.rand(num_rows),
    'column3': np.random.choice(['A', 'B', 'C'], size=num_rows),
}

# 创建dataframe
df = pd.DataFrame(data)

# print(df)
# print("dataframe的长度为: ", len(df))


async def get_data_async(data, start, end):
    """
    异步获取数据，模拟耗时操作
    """
    await asyncio.sleep(random.uniform(0.01, 0.05))  # 模拟网络延迟
    return data[start:end]


async def get_data_api(page=1, page_size=100):
    """
    异步 API 接口，实现分页功能
    """
    start = (page - 1) * page_size
    end = start + page_size
    if end > len(df):
        end = len(df)  # 避免越界
    return await get_data_async(df, start, end)


async def main():
    """
    主程序
    """
    for page in range(1, len(df) // 2):
        # page = 2  # 请求第2页
        page_size = 100  # 每页100条数据
        result = await get_data_api(page, page_size)
        print(f"第{page}页数据: \n{result}")


asyncio.run(main())
