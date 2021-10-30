# Generated by Django 3.2.8 on 2021-10-30 07:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20211030_1233'),
        ('task', '0011_auto_20211030_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 12, 36, 21, 296101)),
        ),
    ]
