#移动端的子路由文件
from django.contrib import admin
from django.urls import path

from mobile.views import index

urlpatterns = [
    path('', index.index, name="mobile_index"),
]
