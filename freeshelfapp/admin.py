from django.contrib import admin
from freeshelfapp.models import Category, Author, Book

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'display_author', 'display_category')
    list_filter = ('date_added', 'author',)