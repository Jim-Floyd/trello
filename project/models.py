from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Auditable(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    is_deleted = models.IntegerField(default=0)
    class Meta:
        abstract = True

class Project(Auditable):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    doc_path = models.CharField(max_length=200)
    closed = models.BooleanField()
    estimated_deadline = models.DateTimeField(null=True)
    class Meta:
        db_table='project'


class ProjectColumns(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    class Meta:
        db_table='project_columns'

