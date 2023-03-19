from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from chat.settings import MEDIA_ROOT
from chats.forms import ResumeForm
from chats.models import ChatModel



User = get_user_model()


def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={'users': users})


def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    # user_access = User.objects.get(username=request.user.username).position.access_level
    if request.user.is_superuser:
        user_access = 1
    else:
        user_access = request.user.position.access_level
    users = User.objects.exclude(username=request.user.username)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect(f'/chat/{username}')
    else:
        form = ResumeForm
    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'

    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    ChatModel.objects.all().update(is_read=1)
    print(MEDIA_ROOT)
    return render(request, 'main_chat.html',
                  context={'user': user_obj, 'users': users, 'messages': message_objs, 'form': form,
                           'user_access': user_access})
