from typing import Dict, List

from django.shortcuts import render


posts: List[Dict[str, str]] = [
    {
        'author': 'Bilel',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Nov 22, 2018',
    },

    {
        'author': 'zennd',
        'title': 'Blog post 1',
        'content': 'Second post content',
        'date_posted': 'Nov 23, 2018',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
