# Generated by Django 3.0.12 on 2021-03-23 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbay', '0009_auto_20210323_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='tags',
        ),
    ]
