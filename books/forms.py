from django import forms
from .models import Genre, Book

# class GenreForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     slug = forms.CharField(label='Slug', max_length=100)
#     description = forms.CharField(widget=forms.Textarea())

class GenreForm(forms.ModelForm):
    slug = forms.RegexField(regex=r'^[\w\-]+$')
    class Meta:
        model = Genre
        fields = ['name', 'slug', 'description']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'slug', 'genre', 'authors', 'price']