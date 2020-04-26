# Generated by Django 2.2 on 2020-04-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='姓名', max_length=16)),
                ('password', models.CharField(help_text='密码', max_length=20)),
                ('phone', models.IntegerField(blank=True, help_text='手机', max_length=11, null=True)),
                ('age', models.IntegerField(blank=True, help_text='年龄', max_length=3, null=True)),
                ('sex', models.IntegerField(blank=True, choices=[(0, '女'), (1, '男'), (2, '保密')], help_text='性别', null=True)),
            ],
        ),
    ]