from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def service_page(request):
    return HttpResponse('这是服务界面')