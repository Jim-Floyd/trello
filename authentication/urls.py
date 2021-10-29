from django.urls import path

from authentication.views import sign_in, home, register

app_name = 'authentication'

urlpatterns = [
    path('', home, name='home'),
    path('login/', sign_in, name='login'),
    path('register/', register, name='register'),
    # path('register_success_page/', register_success_page, name='register_success_page'),
]
