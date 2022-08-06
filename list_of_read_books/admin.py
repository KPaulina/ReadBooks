from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import UserListBooks, ListAuthors

admin.site.register(ListAuthors)
User = get_user_model()


class UserInline(admin.TabularInline):
    model = User


class UserListBooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    readonly_fields = ('timestamp', 'updated')
    raw_id_fields = ['user']


admin.site.register(UserListBooks, UserListBooksAdmin)


