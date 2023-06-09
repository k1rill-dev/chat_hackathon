from django.contrib.auth.hashers import check_password

from chats.models import ChatModel
from .models import User, News, PictureForNews
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UpdateUserForm, UpdatePermissions


def index_main(request):
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return redirect('login')
    count_msg = len(ChatModel.objects.filter(is_read=0))

    fir, sec, thrd = News.objects.all()[:3]
    fp, sp, tp = PictureForNews.objects.get(news=fir), PictureForNews.objects.get(news=sec), PictureForNews.objects.get(news=thrd)

    return render(request, 'main/main.html', {'request': request, 'user': user, 'count_msg': count_msg, 'fir':fir,
                                              'sec': sec,
                                              'thrd': thrd,
                                              'fp': fp,
                                              'sp': sp,
                                              'tp': tp})


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

    lvl = user.position.access_level if user.position is not None else 0

    if request.user.is_superuser or request.user.position.access_level < lvl:
        if request.method == 'POST':
            form = UpdatePermissions(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                dep = cd['department']
                pos = cd['position']
                user.department = dep
                user.position = pos
                user.save()
        else:
            form = UpdatePermissions()

        return render(request, 'main/changable_profile.html', {'form': form, 'user': user, 'f': 1})

    elif user.is_superuser:
        return HttpResponse('батя этого сервера - он, нет прав у тебя другалек')

    elif request.user.position.access_level > user.position.access_level:
        return HttpResponse('У вас недостаточно прав для осуществления')

    else:
        print('збс')
        return render(request, 'main/changable_profile.html', {'user': user, 'f': 2})


def readonly_profile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse('дурак?')

    return render(request, 'main/readonly_profile.html', {'user': user})
