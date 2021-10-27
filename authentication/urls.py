from django.urls import path

from authentication.views import UserCreate, UserLogin

app_name = 'authentication'


urlpatterns = [
    path('register/', UserCreate.as_view(), name = 'register'),
    path('login/', UserLogin.as_view(), name = 'login')
]