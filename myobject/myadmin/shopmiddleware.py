# 自定义中间类（执行是否登录判断）
from django.shortcuts import redirect
from django.urls import reverse

import re


class Shopmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Shopmiddleware")

    def __call__(self, request):
        path = request.path
        print("url:", path)

        # 判断管理后台是否登录
        urllist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin', '/myadmin/verify']
        # 判断当前请求url地址是否以myadmin开头,并且不在urllist中，才做登录判断
        if re.match(r'^/myadmin', path) and (path not in urllist):
            # 判断是否登录（在session中是否有adminuser）
            if 'adminuser' not in request.session:
                # 重定向到登录页面
                return redirect(reverse("myadmin_login"))


        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
