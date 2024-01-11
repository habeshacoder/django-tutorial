from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg


# Create your views here.
def index(request):
    books = Book.objects.all().order_by("title")
    count=books.count()
    average_rating = Book.objects.aggregate(Avg("rating"))
    
    return render(
        request,
        "book/index.html",
        {
            "books": books,
            "avg_rating": average_rating,
            "total_books":count
        },
    )


def book_detailview(request, slug):
    try:
        book = Book.objects.get(slug=slug)

    except:
        raise Http404
    return render(
        request,
        "book/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        },
    )
