from django.urls import path

from .views import HomePageView, AboutPage, BookListView, BookDetailView


urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('about/', AboutPage.as_view(), name='about'),
path('books/', BookListView.as_view(), name='book_list'),
path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]