from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def origin_page(request):
    return HttpResponse("用户界面")


def test_response(request):
    return HttpResponse("测试成功")
