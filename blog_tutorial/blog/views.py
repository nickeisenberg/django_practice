from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'nick eisenberg',
        'title': 'blog post 1',
        'content': 'first post',
        'date_posted': 'july 20 2023'
    },
    {
        'author': 'gunther guntherson',
        'title': 'blog post 2',
        'content': 'gunthers post',
        'date_posted': 'july 21 2023'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})

