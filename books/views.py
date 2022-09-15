from django.views import generic

from .models import Book


class BookListview(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'
