from django.urls import path

from app01 import views

urlpatterns = [
    path('file_upload/', views.FileUpLoadView.as_view(), name="file_upload"),  # 文件上传
    path('data_add/', views.DataAPIView.as_view(), name="data_add"),  # 添加数据
    path('data_get/', views.DataAPIView.as_view(), name="data_get"),  # 查询数据
    path('test_method/<str:data>/', views.test_methods, name="data_get"),  # 测试django自带的方法装饰器
    path('redirect_test/', views.redirect_view, name="redirect_test"),  # 测试redirect重定向
    path('test_get_obj/', views.test_get_obj, name="test_get_obj"),

]