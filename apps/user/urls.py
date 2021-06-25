from django.urls import path
from .views import *
from apps.user.controller import user_login

urlpatterns = [
    # api_test
    path('', origin_page),
    path('api_test/', test_response),

    # login and signup
    path('signup/', user_login.sign_up),
    path('login/', user_login.login),
]
