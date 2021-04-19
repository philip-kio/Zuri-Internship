from django.shortcuts import render, get_object_or_404
from .models import bookStore

# Create your views here.
def home_view(request):
    book= get_object_or_404(bookStore,year_published= 2020)
    book_author = get_object_or_404(bookStore,book_author='Chinua Achebe')
    return render(request, 'home.html', {'book':book,
                                        'book_author':book_author})