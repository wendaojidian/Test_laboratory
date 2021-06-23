from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Permission(models.Model):
    permission_name = models.CharField(max_length=25, unique=True, verbose_name='权限名')
    url = models.URLField(max_length=125, unique=True, null=True, blank=True, verbose_name='URL')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.permission_name

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        db_table = 'tb_permission'


class Role(models.Model):
    role_name = models.CharField(max_length=25, unique=True, verbose_name='角色名')
    permissions = models.ManyToManyField(Permission, blank=True, verbose_name='权限信息')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    # desc = models.CharField(max_length=50, blank=True, null=True, verbose_name='角色描述')

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name
        db_table = 'tb_role'


class User(models.Model):
    user_id = models.CharField(max_length=30, unique=True, primary_key=True, verbose_name='编号')
    user_name = models.CharField(max_length=30, unique=True, verbose_name='用户名')
    real_name = models.CharField(max_length=20, verbose_name='姓名')
    pass_word = models.CharField(max_length=20, default='123456', verbose_name='密码')
    identify = models.CharField(max_length=20, verbose_name='身份信息')
    roles = models.ManyToManyField(Role, blank=True, verbose_name='角色信息')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = 'tb_user'


