from django.db import migrations
import csv
import os.path
from django.conf import settings
from django.core.files import File

def load_book_data(apps, schema_editor):
  
    Book = apps.get_model('freeshelfapp', 'Book')

    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'books.csv')

    with open(datafile) as file: 
        reader = books.csv(file)
        for row in reader:
            book_title = row['title']
            if Book.objects.filter(title=book_title).count():
                continue
            book = Book(
                title=row['title'],
                summary=row['summary'],
                url=row['url'],
            )
            
            book.save()

class Migration(migrations.Migration):

    dependencies = [
        ('freeshelfapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_book_data)
    ]
    