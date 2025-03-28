from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
 username = models.OneToOneField(User, on_delete=models.CASCADE)
 password = models.CharField(max_length=100)
 full_name = models.CharField(max_length=150)
 email = models.EmailField()
 phone = models.CharField(max_length=11)

def __str__(self):
    return self.user.username
