from django.shortcuts import render, get_object_or_404, redirect
from .models import UserListBooks, ListAuthors
from django.urls import reverse_lazy
from .forms import BooksAuthorsForm, BooksForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = UserListBooks
    queryset = UserListBooks.objects.order_by('title')
    context_object_name = 'book_list'


@login_required
def books_list_view(request, id=None):
    qs = UserListBooks.objects.filter(user=request.user)
    context = {
        "book_list": qs
    }
    return render(request, "books/list.html", context)


@login_required
def books_detail_view(request, id=None):
    obj = get_object_or_404(UserListBooks, id=id, user=request.user)
    context = {
        "book": obj
    }
    return render(request, "books/detail.html", context)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = UserListBooks
    fields = ['user', 'title', 'description', 'status']
    success_url = reverse_lazy('list_of_read_books:list')

# def books_add_view(request, id=None):
#     form = BooksAuthorsForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = request.user
#         obj.save()
#         return redirect(obj.get_absolute_url())
#     return render(request, "books/create-update.html", context)


# @login_required
# def books_update_view(request, id=None):
#     obj = get_object_or_404(UserListBooks, id=id, user=request.user)
#     book_form = BooksForm(request.POST or None, instance=obj)
#     author_form = BooksAuthorsForm(request.POST or None)
#     # Formset = modelformset_factory(Model, from=ModelForm, extra=0)
#
#     context = {
#         "form": book_form,
#         "author_form": author_form,
#         "object": obj
#     }
#     if all([book_form.is_valid(), author_form.is_valid()]):
#         book_form = book_form.save(commit=False)
#         book_form.save()
#         author_form = author_form.save(commit=False)
#         author_form.save()
#         obj.user = request.user
#         obj.save()
#         context['message'] = 'Book updated'
#     return render(request, "books/create-update.html", context)
