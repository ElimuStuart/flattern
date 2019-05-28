from django.shortcuts import render
from .models import Post, Category

def index(request):
    return render(request, 'index.html', {})

def blog(request):
    return render(request, 'blog-right-sidebar.html', {})