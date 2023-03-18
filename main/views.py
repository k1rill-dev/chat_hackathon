from django.contrib.auth.hashers import check_password
from .models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UpdateUserForm


def index_main(request):
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return redirect('login')
    return render(request, 'main/main.html', {'request': request, 'user': user})


def view_my_profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            if cd['avatar']:
                user.avatar = request.FILES['avatar']
                user.save()
            if cd['old_passwd'] and cd['passwd'] and cd['passwd1']:
                if check_password(cd['old_passwd'], user.password):
                    if cd['passwd'] == cd['passwd1']:
                        print('ееее, типо сменил пароль, типа умный да да я')
                        user.set_password(cd['passwd'])
                else:
                    return HttpResponse('Ошибка пароля')
            else:
                return redirect('my_p')
    else:
        form = UpdateUserForm()
    return render(request, 'main/my_profile.html', {'request': request, 'user': user, 'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


# TODO: добавить разграничение ролей
def view_another_profile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse('дурак?')
    try:
        user_me = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return HttpResponse('дурак?')

    if user_me.is_superuser:
        return HttpResponse('батя этого сервера - я')

    elif user.is_superuser:
        return HttpResponse('батя этого сервера - он, нет прав у тебя другалек')

    elif user_me.position.access_level > user.position.access_level:
        return HttpResponse('У вас недостаточно прав для осуществления')
    else:
        print('збс')
        return HttpResponse('збс')
