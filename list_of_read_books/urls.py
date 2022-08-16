from django.urls import path
from .views import BookCreateView, BookListView, BookDetailView, BookUpdateView, BookDeleteView
from . import views

app_name = 'list_of_read_books'
urlpatterns = [
    path("", BookListView.as_view(), name='list'),
    path("add", BookCreateView.as_view(), name='add'),
    # path("<int:id>/edit/", views.books_update_view, name='update'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('edit_book/<int:pk>', BookUpdateView.as_view(), name='edit'),
    path('book_delete/<int:pk>', BookDeleteView.as_view(), name='delete')
]
