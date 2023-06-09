from django import forms
from .models import Position, Department

choices = (
    (1, 'Главный'),
    (2, 'Не главный'),
)


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Почтовый адрес"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Пароль"}))


class UpdateUserForm(forms.Form):
    avatar = forms.ImageField(widget=forms.FileInput, required=False, label='Фото профиля')
    old_passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Текущий пароль"}),
                                 label='Текущий пароль', required=False)
    passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Новый пароль"}), label='Новый пароль',
                             required=False)
    passwd1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Повторите пароль"}),
                              label='Подтвердите пароль', required=False)


class UpdatePermissions(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    position = forms.ModelChoiceField(queryset=Position.objects.all())
