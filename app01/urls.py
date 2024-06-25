from django.urls import path

from app01 import views

urlpatterns = [
    path('file_upload/', views.FileUpLoadView.as_view(), name="file_upload"),

]