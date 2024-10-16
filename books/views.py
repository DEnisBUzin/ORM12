from django.shortcuts import render, get_object_or_404

from books.models import Book


def books_view(request):
    book = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': book
    }
    return render(request, template, context)

def show_book(request, id):
    template = 'books/book.html'
    book_id = get_object_or_404(Book, id=id)

    # Поиск предыдущей и следующей книги по дате публикации
    previous_book = Book.objects.filter(pub_date__lt=book_id.pub_date).order_by('-pub_date').first()
    next_book = Book.objects.filter(pub_date__gt=book_id.pub_date).order_by('pub_date').first()

    context = {
        'book': book_id,
        'previous_book': previous_book,
        'next_book': next_book
               }

    return render(request, template, context)