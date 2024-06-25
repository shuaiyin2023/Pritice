import os
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.views import Response, APIView


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
