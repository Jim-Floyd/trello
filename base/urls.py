from .views import home

from django.urls import path

app_name = 'base'
urlpatterns = [
    path('', home, name='home')
]
