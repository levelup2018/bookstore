from django.urls import path
from .views import new_book, like_book, edit_book


urlpatterns = [
    path('new/', new_book),
    path('edit/<int:book_id>/', edit_book),
    path('like-book/', like_book, name='like-book')
]