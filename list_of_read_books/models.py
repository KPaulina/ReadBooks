from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

from .validators import validation_of_status
# Create your models here.


class ListAuthors(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    books = ArrayField(models.CharField(max_length=200), blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class UserListBooks(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author_id = models.ForeignKey(ListAuthors, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=40, validators=[validation_of_status], blank=True) #read #reading #want to read
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('list_of_read_books:detail', kwargs={'id': self.id})

    def get_edit_url(self):
        return reverse('list_of_read_books:update', kwargs={'id': self.id})
