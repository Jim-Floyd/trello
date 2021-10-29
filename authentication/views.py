from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from authentication.models import Employee
from files.utils import store_file


def home(request):
    return render(request, 'home.html', {})

def register_success_page(request):
    return HttpResponse("You have successfully registered. "
                        "We have send activation link to your mail "
                        " Please Activate Your account")

def register(request):
    if request.POST:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        password: str = request.POST.get('password')
        re_password: str = request.POST.get('re_password')
        if not password.__eq__(re_password):
            messages.error(request, 'password does not match')
        else:
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password),
                username=username,
                is_active=0
            )
            user.save()
            employee = Employee(phone_number=phone, user=user)
            file = request.FILES.get('file')
            file_id: int = store_file(file=file)
            employee.image_id = file_id
            employee.save()
            return redirect('authentication:login')

    return render(request, 'register.html', {})


def sign_in(request):
    if request.POST:
        """
        authentication process must be done here
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return reverse_lazy('authentication:home')
        messages.error(request, message='Bad Credentials')
    return render(request, 'login.html', {})

