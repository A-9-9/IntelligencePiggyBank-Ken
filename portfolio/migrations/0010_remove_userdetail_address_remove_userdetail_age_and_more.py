# Generated by Django 4.0.1 on 2022-12-12 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_rename_employee_userdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='annual_income',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='career',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='education',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='gender',
        ),
    ]
