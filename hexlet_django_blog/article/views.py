from django.shortcuts import render

# Create your views here.
# hexlet_django_blog/article/views.py
from django.http import HttpResponse


def index(request):
    return render(
        request,
        "articles/index.html",
        context={
            "app_name": "hexlet_django_blog.article",
        },
    )
