from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from authentication.models import AuthUser


class UserCreate(FormView):
    form_class = UserCreationForm
    redirect_authenticated_user = True
    model = AuthUser
    success_url = reverse_lazy('register')


class UserLogin(LoginView):
    template_name = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')




