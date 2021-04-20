from django.shortcuts import render, get_object_or_404
from .models import bookStore

# Create your views here.
def home_view(request):
    book= bookStore.objects.get(year_published= 2020)
    book_author = bookStore.objects.get(book_author='Chinua Achebe')
    all_books = bookStore.objects.all()
    return render(request, 'home.html',
     {
     'book':book,
     'book_author':book_author,
     'all_books':all_books
                                        }
                                        )