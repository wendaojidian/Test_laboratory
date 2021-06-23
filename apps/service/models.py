from django.db import models
from apps.user.models import *


# Create your models here.
class Software_under_testing(models.Model):
    software_name = models.CharField(max_length=50, unique=True, verbose_name='被测试软件名')
    software_num = models.CharField(max_length=20, unique=True, verbose_name='被测试软件编号')
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
        unique_together = ("software_name", "edition")


class Test_plan(models.Model):
    plan_num = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name='测试计划编号')
    plan_title = models.CharField(max_length=30, verbose_name='测试计划标题')
    plan_software = models.ForeignKey(Software_under_testing, on_delete=models.CASCADE, verbose_name='测试软件名')
    plan_executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='测试计划执行者')
    plan_state = models.CharField(max_length=20, verbose_name='测试计划执行状态')
    plan_desc = models.TextField(verbose_name='测试计划描述')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    test_report = models.FileField(upload_to='test_report')

    def __str__(self):
        return self.plan_title

    class Meta:
        verbose_name = '测试计划'
        verbose_name_plural = verbose_name
        db_table = 'tb_test_plan'


class Test_task(models.Model):
    task_num = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name='测试任务编号')
    task_title = models.CharField(max_length=50, verbose_name='测试任务标题')
    task_executor = models.ManyToManyField(User, verbose_name='测试任务执行者')
    task_state = models.CharField(max_length=20, verbose_name='测试任务状态')
    task_desc = models.TextField(verbose_name='测试任务描述')
    task_plan = models.ForeignKey(Test_plan, on_delete=models.CASCADE, verbose_name='测试任务所属计划')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.task_title

    class Meta:
        verbose_name = '测试任务'
        verbose_name_plural = verbose_name
        db_table = 'tb_test_task'


class Test_case(models.Model):
    case_num = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name='测试用例编号')
    case_title = models.CharField(max_length=50, verbose_name='测试用例标题')
    case_state = models.CharField(max_length=20, verbose_name='测试用例状态')
    case_executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='测试用例执行者',
                                      related_name='case_executor')
    case_assessor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='测试用例评审员',
                                      related_name='case_assessor')
    case_requisite = models.TextField(blank=True, verbose_name='测试输入项')
    case_process = models.TextField(verbose_name='测试步骤')
    expected_results = models.TextField(verbose_name='预期结果')
    actual_results = models.TextField(verbose_name='实际结果')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    nothing = models.CharField(max_length=10, verbose_name='nothing')

    def __str__(self):
        return self.case_title

    class Meta:
        verbose_name = '测试用例'
        verbose_name_plural = verbose_name
        db_table = 'tb_test_case'
