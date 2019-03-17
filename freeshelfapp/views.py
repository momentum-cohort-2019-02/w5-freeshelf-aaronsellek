from django.shortcuts import render, get_object_or_404, redirect
from freeshelfapp.models import Category, Author, Book
from django.views import generic
from freeshelfapp.forms import RegisterForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):

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

@require_http_methods(['POST'])
@login_required
def book_favorite_view(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    next = request.POST.get('next', '/')

    favorite, created = request.user.favorite_set.get_or_create(book=book)

    if created: 
        messages.success(request, f"favorited {book.title}")
    else: 
        messages.info(request, f"unfavorited {book.title}")
        favorite.delete()

    return HttpResponseRedirect(next)
    
class CategoryDetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


