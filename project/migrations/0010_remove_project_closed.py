# Generated by Django 3.2.8 on 2021-10-30 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20211030_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='closed',
        ),
    ]
