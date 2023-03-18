from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Почтовый адрес"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Пароль"}))


class UpdateUserForm(forms.Form):
    avatar = forms.ImageField(widget=forms.FileInput)
    old_passwd = forms.CharField(widget=forms.PasswordInput)
    passwd = forms.CharField(widget=forms.PasswordInput)
    passwd1 = forms.CharField(widget=forms.PasswordInput)


