from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # 'index' - bu asosiy sahifangizning URL nomi
        else:
            return render(request, 'login.html', {'message': 'Username yoki parol noto\'g\'ri'})
    else:
        return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Muvaffaqiyatli login qilinganidan keyin bosh sahifaga
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def base_view(request):
    return render(request, 'index.html')
