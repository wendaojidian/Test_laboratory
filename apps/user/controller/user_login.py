from django.http import HttpResponse, JsonResponse
from apps.user.models import *
import json
from utils.util_out_print import out_print_request
from utils.util_jwt import *
from apps.user.dao.user_dao import *


# 暂时只考虑测试leader和测试工程师
def sign_up(request):
    """
    注册功能
    :param request:
    :return: 成功或失败的字符串
    """
    if request.method == 'POST':
        request.params = json.loads(request.body)
        out_print_request(request)

        jwt_token = request.params['jwt_info']
        decoding_msg = jwt_decoding(jwt_token)

        payload = decoding_msg["payload"]
        return_msg = decoding_msg["msg"]

        if not payload:
            return HttpResponse(return_msg)
        else:
            return_msg = create_user(payload)
            return HttpResponse(return_msg)


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_obj = User.objects.filter(username=username, password=password).first()
