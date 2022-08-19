from .models import UserListBooks, ListAuthors
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = UserListBooks
    queryset = UserListBooks.objects.order_by('title')
    context_object_name = 'book_list'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = UserListBooks
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = UserListBooks
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('list_of_read_books:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = UserListBooks
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('list_of_read_books:list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionError
        return super().dispatch(request, *args, **kwargs)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = UserListBooks
    success_url = reverse_lazy('list_of_read_books:list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionError
        return super().dispatch(request, *args, **kwargs)


