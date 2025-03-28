from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from accounts.models import Profile


def register(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Это имя пользователя уже занято. Пожалуйста, выберите другое.')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, full_name=full_name, phone=phone, email=email)
        messages.success(request, 'Вы успешно зарегистрированы!')
        return redirect('index')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(f"Attempting to log in with Username: {username}, Password: {password}")

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы авторизованы')
            return redirect('index')
        else:
            print(f"Login failed for user: {username}")
            messages.error(request,'Неверный логин или пароль')
            return render(request, 'login.html')

    return render(request, 'login.html')

def index_view(request):
    return render(request, 'index.html')