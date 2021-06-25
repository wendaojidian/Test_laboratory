from django.http import HttpResponse, JsonResponse
from apps.user.models import *
import json




# 暂时只考虑测试leader和测试工程师
def sign_up(request):
    if request.method == 'POST':
        request.params = json.loads(request.body)
        username = request.params["username"]
        return JsonResponse({"username": username})
    return HttpResponse('123')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_obj = User.objects.filter(username=username, password=password).first()
