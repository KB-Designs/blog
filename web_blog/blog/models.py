from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField(default="NO CONTENT")
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)



class Meta:
    odering=('-publish',)

def __str__(self):
    return self.title




# Create your models here.