
from django.db import models

from authentication.models import AuthUser
from project.models import ProjectColumns, Auditable, ProjectMember


# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    projectcolumn = models.ForeignKey(ProjectColumns, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'

class Comments(models.Model):
    comment = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    class Meta:
        db_table = 'comment'


class UploadComment(models.Model):
    original_name = models.CharField(max_length=300)
    content_type = models.CharField(max_length=100)
    new_name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    code = models.CharField(max_length=70, unique=True)
    size = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    class Meta:
            db_table = 'upload_comment'