from django.db import models
from django.contrib.auth.models import User


class Auditable(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.IntegerField(default=0)



