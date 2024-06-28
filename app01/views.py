import os
import datetime
from django.utils import timezone
from django.db.models import Avg, F
from functools import wraps
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core import serializers

from rest_framework import status
from rest_framework.views import Response, APIView

from app01.models import *


def upload_file_in_chunks(file, chunk_size=1024 * 1024):
    """
    分片上传文件的函数

    参数:
    file_path (str): 要上传的文件路径
    chunk_size (int): 每个分片的大小，默认为1MB

    返回:
    None
    """
    print("\n\n")
    print("开始上传文件*************\n\n")
    cache_path = fr"D:\Company-yin\Files\上传文件_cache\{file.name}"  # 文件缓存路径
    # 打开文件
    # with open(file_path, 'rb') as file:
    chunk_number = 0
    while True:
        # 读取文件分片
        chunk = file.read(chunk_size)
        if not chunk:
            # 如果分片为空，说明文件已经读取完毕
            break

        chunk_number += 1
        # 模拟上传分片的过程
        print(f"正在上传第 {chunk_number} 个分片，大小为 {len(chunk)} 字节")
        # 这里可以调用实际的上传函数，例如：upload_chunk(chunk)
        if not os.path.exists(cache_path):
            os.makedirs(cache_path)
        chunk_path = os.path.join(cache_path, f"chunk_{chunk_number}")
        with open(chunk_path, 'wb') as chunk_file:
            chunk_file.write(chunk)

    print("文件上传完成")
    return cache_path


def merge_chunks(chunk_paths, output_path):
    """
    合并分片文件为一个完整的文件

    参数:
    chunk_paths (list): 分片文件路径列表
    output_path (str): 合并后的文件输出路径

    返回:
    None
    """

    print("开始合并文件*************\n\n")
    with open(output_path, 'wb') as output_file:
        for chunk_path in chunk_paths:
            with open(chunk_path, 'rb') as chunk_file:
                output_file.write(chunk_file.read())
            # 可选：合并后删除分片文件
            # os.remove(chunk_path)

    print("文件合并完成")

    return True


# 文件上传
class FileUpLoadView(APIView):

    # 简单文件上传
    def post_1(self, request):
        file = request.FILES["file"]
        print("上传的文件: \n", file)
        print("文件名: \n", file.name)

        # 文件内容
        # with open(file, "rb") as f:
        # file_content = file.read()
        # print("上传文件的内容: \n", file_content)

        # 文件保存路径
        file_path = fr"D:\Company-yin\Files\上传文件_test\{file.name}"
        print("文件保存路径: ", file_path)
        with open(file_path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)

        return HttpResponse("上传成功")

    # 文件分片上传
    def post(self, request):
        file = request.FILES["file"]

        file_path = fr"D:\Company-yin\Files\上传文件_test\{file.name}"  # 文件保存路径
        # cache_path = fr"D:\Company-yin\Files\上传文件_cache\{file.name}"  # 文件缓存路径

        ''' 将文件分片 '''
        chunk_size = 1024 * 1024
        cache_path = upload_file_in_chunks(file, chunk_size)

        # 从缓存路径中将对应文件的所有分片读取到
        chunk_paths = os.listdir(cache_path)
        chunk_paths = [os.path.join(cache_path, chunk_path) for chunk_path in chunk_paths]

        ''' 将分片好的文件合并 '''
        result = merge_chunks(chunk_paths, file_path)
        if result:
            return JsonResponse({"msg": "上传成功"}, status=200)
        else:
            return JsonResponse({"msg": "上传失败"}, status=500)


@csrf_exempt
def file_upload(request):
    file = request.FILES["file"]
    print("上传的文件: \n", file)
    print("文件名: \n", file.name)

    # 文件内容
    # with open(file, "rb") as f:
    # file_content = file.read()
    # print("上传文件的内容: \n", file_content)

    # 文件保存路径
    file_path = fr"D:\Company-yin\Files\上传文件_test\{file.name}"
    print("文件保存路径: ", file_path)
    with open(file_path, "wb") as f:
        for chunk in file.chunks():
            f.write(chunk)

    return HttpResponse("上传成功")


class DataAPIView(APIView):

    def get_1(self, request):
        # data = Student.objects.raw("SELECT * FROM app01_student")
        data = Student.objects.all()
        for obj in data:
            print(obj.name)
            print(type(obj))

        return Response({"data": data.values()}, status=status.HTTP_200_OK)

    @staticmethod
    def format_time(time_obj):
        return time_obj.strftime("%Y-%m-%d %H:%M:%S")

    def get(self, request):
        data = Student.objects.aggregate(Avg("age"))  # aggregate()对queryset总体进行聚合(这里是求所有学生的平均年龄)
        query_set = Student.objects.annotate(avg_age=Avg("age"))  # annotate()对queryset的每一条记录进行聚合(这里是求的每条记录的平均年龄)

        for item in query_set:
            item.create_time = self.format_time(item.create_time)
            item.update_time = self.format_time(item.update_time)

        serializer_data = [
            {
                "id": obj.id,
                "create_time": obj.create_time,
                "update_time": obj.update_time,
                "name": obj.name,
                "age": obj.age,
                "email": obj.email,
                "number": obj.number,
                "gender": obj.get_gender_display(),
                "avg_age": obj.avg_age
            }
            for obj in query_set
        ]

        # data = serializers.serialize("json", data, fields=("name", "age", "create_time", "gender"))
        # data = serializers.serialize("json", data)

        # return JsonResponse(query_set, safe=False, status=status.HTTP_200_OK)
        # return HttpResponse(data, content_type="application/json", status=200)
        return Response({"data": serializer_data, "avg_age": data["age__avg"]}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        # key = "Postman-Token"
        # print(request.headers)
        # token = "a900def9-a5dc-4ba3-942b-dedc785e0818"
        # if request.headers[key] != token:
        #     return Response({"msg": "Token错误"}, status=status.HTTP_401_UNAUTHORIZED)

        Student.objects.create(**data)

        return Response({"msg": "添加成功"}, status=status.HTTP_201_CREATED)


@require_http_methods(["GET", "POST"])
@csrf_exempt
def test_methods(request, data):
    print("接收的data: ", data)
    print("发起的请求类型正确")
    return HttpResponse("请求成功")


def redirect_view(request):
    obj = Student.objects.get(pk=1)
    # return redirect(test_methods, data=obj.name)  # 重定向到test_methods试图，并传递参数data
    return redirect("https://www.baidu.com/")


def out_side(func_name):
    """
    装饰器函数，用于测试装饰器
    """

    @wraps(func_name)
    def inner_func(request, *args, **kwargs):
        print("函数执行之前调用")
        response = func_name(request, *args, **kwargs, content={"name": "yinshuai", "data": 13123})  # content参数用于传递额外参数
        print("函数执行之后调用")
        return response

    return inner_func


@out_side
def test_get_obj(request, *args, **kwargs):
    data = kwargs.get("content")  # 获取装饰器传递的额外参数
    print("从装饰器函数中返回的数据: ", data)

    print("已经成功调用装饰器函数了")
    data = get_list_or_404(Student, age__gt=20)
    print(data)
    return HttpResponse(data, status=200)
