from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class FileMessage(models.Model):
    file = models.FileField(upload_to='', null=True)

    def __str__(self) -> str:
        return self.file


class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    # file_id = models.OneToOneField(FileMessage, on_delete=models.CASCADE, null=True)
    type_msg = models.CharField(null=True, blank=True, max_length=10)
    is_read = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.message
