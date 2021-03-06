# Generated by Django 2.0.1 on 2018-02-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('txdemo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('object_id', models.CharField(default='', max_length=5, primary_key=True, serialize=False, verbose_name='主键')),
                ('name', models.CharField(max_length=10, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=20, verbose_name='联系地址')),
                ('message', models.CharField(max_length=50, verbose_name='简介')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
