from django.contrib.auth.models import User
from django.db import models
class Phone(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    