from django.db import models
from apps.user.models import *


# Create your models here.
class Software_under_testing(models.Model):
    software_name = models.CharField(max_length=50, unique=True, primary_key=True, verbose_name='被测试软件名')
    edition = models.CharField(max_length=20, verbose_name='版本号')
    software_type = models.CharField(max_length=20, verbose_name='被测试软件类型')
    software_data = models.FileField(upload_to='software')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.software_name+self.edition

    class Meta:
        verbose_name = '被测试软件'
        verbose_name_plural = verbose_name
        db_table = 'tb_software_under_testing'


class Test_plan(models.Model):
    plan_num = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name='测试计划编号')
    plan_title = models.CharField(max_length=30, verbose_name='测试计划标题')
    plan_software = models.ForeignKey(Software_under_testing, on_delete=models.CASCADE)
    plan_executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.plan_title

    class Meta:
        verbose_name = '被测试软件'
        verbose_name_plural = verbose_name
        db_table = 'tb_test_plan'
