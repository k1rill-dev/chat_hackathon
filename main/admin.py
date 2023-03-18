from django.contrib import admin
from .models import User, News, Position, Department
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    ...

admin.site.register(User, CustomUserAdmin)
admin.site.register(News)
admin.site.register(Position)
admin.site.register(Department)
