from django.urls import path
from .views import index_main, view_my_profile, user_login

urlpatterns = [
    path('', index_main, name='index'),
    path('my_profile', view_my_profile, name='my_p'),
    path('login/', user_login, name='login')
]