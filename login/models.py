from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    birth = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    