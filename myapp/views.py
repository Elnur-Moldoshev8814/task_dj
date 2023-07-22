from django.shortcuts import render
from .models import Author, Post, Category


def all_posts(request):
    a = Post.objects.all()
    return render(
        request,
        template_name='app/home.html',
        context={'a': a}
    )
