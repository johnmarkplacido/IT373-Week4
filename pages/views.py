from django.shortcuts import render
from .models import Book, Category

# Main view for the library
def home(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'books': books,
        'categories': categories
    })

def about(request):
    return render(request, 'about.html', {"title": "About"})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)