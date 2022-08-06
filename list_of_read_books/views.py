from django.shortcuts import render, get_object_or_404, redirect
from .models import UserListBooks
from .forms import BooksForm
from django.contrib.auth.decorators import login_required
# Create your views here.


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
        "book_list": qs
    }
    return


@login_required
def books_add_view(request, id=None):
    form = BooksForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "books/create-update.html", context)


@login_required
def books_update_view(request, id=None):
    obj = get_object_or_404(UserListBooks, id=id, user=request.user)
    form = BooksForm(request.POST or None, instance=obj)
    context = {
        "form": form,
        "object": obj
    }
    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        context['message'] = 'Book updated'
    return render(request, "books/create-update.html", context)
