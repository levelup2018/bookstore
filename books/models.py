from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    slug = models.SlugField(max_length=100, verbose_name=_('Slug'))
    genre = models.ForeignKey('Genre',
        null=True, blank=True,
        on_delete=models.SET_NULL, verbose_name=_('Genre'))
    authors = models.ManyToManyField('Author')
    cover = models.ImageField(upload_to='book_cover', blank=True, null=True)
    price = models.IntegerField(default=0)
    user = models.ForeignKey('auth.User',
        null=True, blank=True,
        on_delete=models.SET_NULL)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    popular = models.BooleanField(default=False)
    description = models.TextField()

    def total_books(self):
        return Book.objects.filter(genre=self).count()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    is_modern = models.BooleanField(default=False)

    def __str__(self):
        return self.name
