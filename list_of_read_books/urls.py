from django.urls import path
from .views import BookCreateView, BookListView
from . import views

app_name = 'list_of_read_books'
urlpatterns = [
    path("", BookListView.as_view(), name='list'),
    path("add", BookCreateView.as_view(), name='add'),
    # path("<int:id>/edit/", views.books_update_view, name='update'),
    path("<int:id>", views.books_detail_view, name='detail'),
]
