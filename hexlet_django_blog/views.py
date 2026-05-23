# hexlet_django_blog/views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))

def about(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )
