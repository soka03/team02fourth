from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    location = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.nickname

# board.models로 위치 옮겨야 함

from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    # image_url = models.URLField()
    
    def __str__(self):
        return self.name