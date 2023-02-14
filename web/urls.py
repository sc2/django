#前台大堂点餐的子路由文件
from django.contrib import admin
from django.urls import path, include

from web.views import index

urlpatterns = [
    path('', index.index, name="web_index"),

    # 前台登录、退出路由
    path('login', index.login, name="web_login"),  # 加载登录表单
    path('dologin', index.dologin, name="web_dologin"),  # 执行登录表单
    path('logout', index.logout, name="web_logout"),  # 退出登录表单
    path('verify', index.verify, name="web_verify"),  # 输出验证码

    # 为url路由添加请求前缀
    path("web/", include([
        path('', index.webindex, name="web_index"),
    ]))


]
