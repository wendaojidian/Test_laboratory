from django.urls import path
from .views import *

urlpatterns = [
    path('', origin_page),
    path('test/', test_response),
]
