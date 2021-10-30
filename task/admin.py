from django.contrib import admin
from .models import Task, TaskColumn

admin.site.register(Task)
admin.site.register(TaskColumn)

# Register your models here.
