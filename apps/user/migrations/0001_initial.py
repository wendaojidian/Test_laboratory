# Generated by Django 3.2 on 2021-06-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=25, unique=True, verbose_name='权限名')),
                ('url', models.URLField(blank=True, max_length=125, null=True, unique=True, verbose_name='URL')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '权限',
                'verbose_name_plural': '权限',
                'db_table': 'tb_permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=25, unique=True, verbose_name='角色名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('permissions', models.ManyToManyField(blank=True, to='user.Permission', verbose_name='权限信息')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
                'db_table': 'tb_role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='编号')),
                ('user_name', models.CharField(max_length=30, unique=True, verbose_name='用户名')),
                ('real_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('pass_word', models.CharField(default='123456', max_length=20, verbose_name='密码')),
                ('identify', models.CharField(max_length=20, verbose_name='身份信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('roles', models.ManyToManyField(blank=True, to='user.Role', verbose_name='角色信息')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'tb_user',
            },
        ),
    ]
