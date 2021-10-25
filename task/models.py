
from django.db import models

from project.models import ProjectColumns, Auditable, ProjectMember


# Create your models here.


class Task(Auditable):
    name = models.CharField(max_length=200)
    description = models.TextField()
    column_id=models.ForeignKey(ProjectColumns, on_delete=models.CASCADE)
    class Meta:
        db_table='task'

class TaskMember(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    user = models.ForeignKey(ProjectMember, on_delete=models.CASCADE)