from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choice = [
        ['admin', 'Admin'],
        ['user', 'User'],
    ]
    role = models.CharField(max_length=10, choices=choice, default="user")
    def __str__(self):
        return f'{self.user} - {self.role}'