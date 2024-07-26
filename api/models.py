from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    
    title= models.CharField(max_length=100, null=True)
    content=models.CharField(max_length=100, null=True, blank=True)
    date_posted=models.DateTimeField(auto_now_add=True, null=True)
    deadline=models.DateTimeField(null=True)
    user=models.ForeignKey(User, max_length=100, on_delete=models.CASCADE, null=True)
    