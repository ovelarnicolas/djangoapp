from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book


def Home(request):
    num_books = Book.objects.all().count()    
    num_books_user = Book.objects.filter(user=request.user).count()    
    template_name = 'book/index.html'
    return render(request, template_name, context={'num_books': num_books, 'num_books_user': num_books_user})
