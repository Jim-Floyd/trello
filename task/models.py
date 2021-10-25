from django.db import models
from utils.utils import Auditable


# Create your models here.


class Task(Auditable):
    name = models.CharField(max_length=200)
    description = models.TextField()
