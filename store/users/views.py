from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        #Проверяем на валидность.
        if form.is_valid():
            #Достаем поля из формы.
            username = request.POST['username']
            password = request.POST['password']
            #Подтверждаем подлиность.
            user = auth.authenticate(username=username, password=password)
            #Если пользователь найден авторизовываем его.
            if user:
                auth.login(request, user)
                # Перенаправляем пользователя на страницу
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        print('1')
        if form.is_valid():
            form.save()
            print('2')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
        print('3')
    context = {'form': form}
    return render(request, 'users/register.html', context)

