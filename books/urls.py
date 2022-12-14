from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListview.as_view(), name='books_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail')
]
