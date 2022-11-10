from django.views.generic import TemplateView, ListView, DetailView

from .models import Book



class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'app/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'app/book_detail.html'