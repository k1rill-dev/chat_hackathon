from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

choices = (
    (1, 'Главный'),
    (2, 'Не главный'),
)


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar_user/%Y/%m/%d/', blank=True, null=True,
                               default='Нет картинки',
                               verbose_name='Главное изображение')
    email = models.EmailField(_("email address"), unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Отдел', null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE, verbose_name='Должность', null=True, blank=True)
    key_aes = models.CharField('Key Aes', null=True, max_length=100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']




class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название отдела')

    def __str__(self):
        return f'{self.name}'


class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название должности')
    access_level = models.IntegerField(verbose_name='Уровень доступа', choices=choices)


    def __str__(self):
        return f'{self.name} с {self.access_level} уровнем доступа'


class PictureForNews:
    picture = models.ImageField(upload_to='pictures_news/%Y/%m/%d/', blank=True, null=True,
                                default='Нет картинки',
                                verbose_name='Изображение')
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name='Новость')


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=300, verbose_name='Описание')
    body = models.CharField(max_length=7878, verbose_name='Тело новости')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f'{self.title}'
