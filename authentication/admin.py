from django.contrib import admin

# Register your models here.
from authentication.models import AuthUser

admin.site.register(AuthUser)