from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    message = models.CharField(max_length=100, null=True)
    #좋아요한 가게들이 들어있는 정보 리스트
