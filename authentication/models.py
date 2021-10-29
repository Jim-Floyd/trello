from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from files.models import UploadUser


# Create your models here.
class Employee(models.Model):
    birth_date = models.DateTimeField(null=True)
    image = models.OneToOneField(UploadUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'Employee'


class Role(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    class Meta:
        db_table = 'auth_role'