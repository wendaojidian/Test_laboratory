from django.urls import path
from .views import *

urlpatterns = [
    path('', service_page),
    path('jsontry/', json_try)
]
