from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListview.as_view(), name='books_list')
]
