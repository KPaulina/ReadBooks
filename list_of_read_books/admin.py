from django.contrib import admin

# Register your models here.
from .models import UserListBooks, ListAuthors


class UserListBooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    readonly_fields = ['user', 'timestamp']


admin.site.register(UserListBooks)
admin.site.register(ListAuthors)

