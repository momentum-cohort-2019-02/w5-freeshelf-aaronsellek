from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('author/<slug:slug>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/<int:book_pk>/favorite/', views.book_favorite_view, name="book_favorite"),
]