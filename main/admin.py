from django.contrib import admin
from .models import User, News, Position, Department
from django.contrib.auth.admin import UserAdmin
from django import forms

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2",
                           "first_name", "last_name", "email",
                           "is_active", "avatar", "department", "position",
                           "groups"),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(News)
# admin.site.register(User)
admin.site.register(Position)
admin.site.register(Department)
