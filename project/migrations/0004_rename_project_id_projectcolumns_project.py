# Generated by Django 3.2.8 on 2021-10-27 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_projectmember_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectcolumns',
            old_name='project_id',
            new_name='project',
        ),
    ]
