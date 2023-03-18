# Generated by Django 4.1.7 on 2023-03-18 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_position_access_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureForNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='Нет картинки', null=True, upload_to='pictures_news/%Y/%m/%d/', verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.news', verbose_name='Новость')),
            ],
        ),
    ]
