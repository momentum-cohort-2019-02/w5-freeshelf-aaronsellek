from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    """Model representing a book category."""
    name = models.CharField(max_length=200, help_text='Enter category')
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        if self.slug:
            return
        base_slug = slugify(self.name)
        slug = base_slug
        n = 0
        while Category.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        self.slug =slug

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.slug)])
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        if self.slug:
            return
        base_slug = slugify(self.name)
        slug = base_slug
        n = 0
        while Category.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        self.slug =slug

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.slug)])

    def __str__(self):
        return self.name
      
class Book(models.Model):
    title = models.CharField(max_length=75)

    author = models.ManyToManyField(Author)

    summary = models.TextField(max_length=500, help_text='Enter description of book')
    
    date_added = models.DateField(null=True, blank=True)

    category = models.ManyToManyField(Category, help_text='Select  category for  book')

    url = models.URLField(max_length=150, null=True, blank=True)
    picture = models.ImageField(upload_to='books/', null=True, blank=True)

    favorited_by = models.ManyToManyField(to=User, related_name='favorite_books', through='Favorite')

    class Meta:
        ordering = ['-date_added',]

    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])

    display_category.short_description = 'category'

    def display_author(self):
        return ', '.join(author.name for author in self.author.all()[:3])

    display_author.short_description = 'author'

    def display_favorited_by(self):
        return ', '.join(favorited_by.username for favorited_by in self.favorited_by.all()[:3])

    display_favorited_by.short_description = 'favorited_by_user'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)
