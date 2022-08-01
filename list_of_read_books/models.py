from django.db import models
from django.conf import settings
# Create your models here.


class UserListBooks(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    review = models.TimeField(null=True)
    category = models.CharField(max_length=50) #read #reading #want to read
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ListAuthors(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    name_surname = models.ForeignKey(UserListBooks, on_delete=models.CASCADE)
    books = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
