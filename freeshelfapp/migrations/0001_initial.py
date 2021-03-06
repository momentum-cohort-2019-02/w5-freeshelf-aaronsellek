# Generated by Django 2.1.7 on 2019-03-16 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('summary', models.TextField(help_text='Enter description of book', max_length=500)),
                ('date_added', models.DateField(blank=True, null=True)),
                ('url', models.URLField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='books/')),
                ('author', models.ManyToManyField(to='freeshelfapp.Author')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter category', max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorited_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freeshelfapp.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(help_text='Select  category for  book', to='freeshelfapp.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_books', through='freeshelfapp.Favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
