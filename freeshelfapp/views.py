from django.shortcuts import render, get_object_or_404
from freeshelfapp.models import Category, Author, Book
from django.views import generic

def index(request):
    """View function for home page of site."""

    categories = Category.objects.all()
    books = Book.objects.all()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
       'categories': categories,
       'books': books,
       'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)
