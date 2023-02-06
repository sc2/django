from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def index(request):
    """大唐点餐前台"""
    return render(request, "web/index.html")
