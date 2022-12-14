from django.views import generic

from .models import Book


class BookListview(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
