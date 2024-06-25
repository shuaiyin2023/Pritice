from django.urls import path

from app01 import views

urlpatterns = [
    path('file_upload/', views.FileUpLoadView.as_view(), name="file_upload"),  # 文件上传
    path('data_add/', views.DataAPIView.as_view(), name="data_add"),  # 添加数据
    path('data_get/', views.DataAPIView.as_view(), name="data_get"),  # 查询数据

]