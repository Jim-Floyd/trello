from django.db import models
from files.models import UploadUser


# Create your models here.
class AuthUser(models.Model):
    image = models.OneToOneField(UploadUser, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    email = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=200)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    is_super_admin = models.BooleanField()

    class Meta:
        db_table = 'Users'


class Role(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    class Meta:
        db_table = 'auth_role'


class Status(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    class Meta:
        db_table = 'auth_status'


class Employee(models.Model):
    address = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'auth_employee'


