from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def service_page(request):
    return HttpResponse('这是服务界面')


def json_try(request):
    return JsonResponse({'ret': 1, 'msg': '这是json返回'})
