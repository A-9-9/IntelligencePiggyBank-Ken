# Generated by Django 4.0.1 on 2022-11-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('full_name', models.TextField()),
                ('industry_code', models.IntegerField()),
                ('recommend_score', models.FloatField()),
                ('introduction', models.TextField()),
                ('link_yahoo_finance', models.TextField()),
                ('link_official_website', models.TextField()),
            ],
        ),
    ]