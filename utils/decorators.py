# 此文件用于存放各种装饰器函数
from functools import wraps


def out_side(func_name):
    """
    装饰器函数，用于测试装饰器
    """

    @wraps(func_name)
    def inner_func(request, *args, **kwargs):
        print("函数执行之前调用")
        response = func_name(request, *args, **kwargs, content={"name": "yinshuai", "data": 13123})  # content参数用于传递额外参数
        print("函数执行之后调用")
        # raise Exception("测试异常")
        return response

    return inner_func