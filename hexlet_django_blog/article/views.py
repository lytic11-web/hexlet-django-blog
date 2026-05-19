from django.shortcuts import render

# Create your views here.
# hexlet_django_blog/article/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("article")
