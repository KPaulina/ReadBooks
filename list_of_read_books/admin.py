from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import UserListBooks, ListAuthors

admin.site.register(ListAuthors)
User = get_user_model()


class UserInline(admin.TabularInline):
    model = User


class UserListBooksAuthorsInline(admin.StackedInline):
    model = ListAuthors
    extra = 0
    # fields = ('name', 'surname')


class UserListBooksAdmin(admin.ModelAdmin):
    inlines = [UserListBooksAuthorsInline]
    list_display = ('title', 'category')
    readonly_fields = ('timestamp', 'updated')
    raw_id_fields = ['user']


admin.site.register(UserListBooks, UserListBooksAdmin)


