# Generated by Django 4.0.1 on 2022-11-27 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_assetsdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetsdetail',
            name='industry_code',
            field=models.FloatField(),
        ),
    ]
