from django.contrib import admin
from .models import User, News, Position, Department, PictureForNews
from django.contrib.auth.admin import UserAdmin
from django import forms


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('first_name', 'last_name', 'position', 'department', 'email')
    list_display_links = ('first_name', 'last_name', 'position', 'department', 'email')
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password",
                           "first_name", "last_name", "email",
                           "is_active", "avatar", "department", "position",),
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ("first_name", "last_name",'position', 'department', 'email',)}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(News)
admin.site.register(Position)
admin.site.register(PictureForNews)
admin.site.register(Department)
