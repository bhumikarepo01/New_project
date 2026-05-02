from django.shortcuts import render, get_object_or_404, redirect
from .models import Author
from .forms import AuthorForm,BookForm


# List Authors
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


# Add Author
def author_create(request):
    form = AuthorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('author_list')

    return render(request, 'author_form.html', {'form': form})


# Author Detail + Books
def author_detail(request, pk):
    author = get_object_or_404(Author, id=pk)
    books = author.books.all()   # Display books of that author

    return render(request, 'author_detail.html', {
        'author': author,
        'books': books
    })

def book_create(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('author_list')

    return render(request, 'book_form.html', {'form': form})