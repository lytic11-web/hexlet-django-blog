from django.shortcuts import render

# Create your views here.
# hexlet_django_blog/article/views.py
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "articles/index.html",
            context={
                "app_name": "hexlet_django_blog.article",
            },
        )
