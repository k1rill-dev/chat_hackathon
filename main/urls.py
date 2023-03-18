from django.urls import path
from .views import index_main, view_my_profile, user_login, view_another_profile, readonly_profile

urlpatterns = [
    path('', index_main, name='index'),
    path('my_profile', view_my_profile, name='my_p'),
    path('login/', user_login, name='login'),
    path('profile/<int:pk>', view_another_profile, name='v_profile'),
    path('ro_profile/<int:pk>', readonly_profile, name='ro_profile')
]