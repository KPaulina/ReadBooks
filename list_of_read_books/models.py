from django.db import models
from django.conf import settings
from .validators import validation_of_status
# Create your models here.


class ListAuthors(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    books = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class UserListBooks(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author_id = models.ForeignKey(ListAuthors, on_delete=models.PROTECT, null=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=40, validators=[validation_of_status], blank=True) #read #reading #want to read
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



