# Generated by Django 3.2 on 2021-06-23 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test_plan',
            options={'verbose_name': '被测试软件', 'verbose_name_plural': '被测试软件'},
        ),
        migrations.AlterModelTable(
            name='test_plan',
            table='tb_test_plan',
        ),
    ]