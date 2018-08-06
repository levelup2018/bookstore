from django.shortcuts import render
from .models import Book, Genre
from .forms import BookForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def like_book(request):
    if 'likes' not in request.session:
        request.session['likes'] = []
    new_val = int(request.GET['id'])
    if 'unlike' in request.GET:
        request.session['likes'].remove(new_val)
        request.session.modified = True
    elif new_val not in request.session['likes']:
        request.session['likes'].append(new_val)
        request.session.modified = True
    import pdb
    pdb.set_trace()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def all_books(request):
    books = Book.objects.filter(is_approved=True)
    genre = None
    if 'genre_id' in request.GET:
        genre = Genre.objects.get(id=int(request.GET['genre_id']))
        books = books.filter(genre=genre)

    if 'search' in request.GET:
        books = books.filter(name__contains=request.GET['search'])

    p = Paginator(books, 3)

    return render(request, 'books/all_books.html', {
            'books': p.page(request.GET.get('page', 1)),
            'paginator': p,
            'genre': genre
        })

def new_book(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            inst = form.save()
            inst.user = request.user
            inst.save()

            messages.add_message(
                request, messages.INFO, 
                'Book {} успешно создан'.format(inst.name))

            return HttpResponseRedirect('/books/new/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()
    return render(request, 'books/new_book.html', {
        'form': form
    })


def edit_book(request, book_id):
    # if not Book.objects.filter(id=book_id).exists():
    #     return HttpResponseNotFound()

    # try:
    #     book = Book.objects.get(id=book_id)
    # except Book.DoesNotExist :
    #     return HttpResponseNotFound()

    book = get_object_or_404(Book, id=book_id)

    if request.user != book.user:
        return HttpResponseNotFound()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST, instance=book)
        # check whether it's valid:
        if form.is_valid():
            inst = form.save()
            inst.user = request.user
            inst.save()

            messages.add_message(
                request, messages.INFO, 
                'Book {} успешно изменен'.format(inst.name))

            return HttpResponseRedirect('/books/new/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm(instance=book)
    return render(request, 'books/new_book.html', {
        'form': form
    })