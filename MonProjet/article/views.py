from django.shortcuts import render
from django.http import HttpResponse


def index(request, *args, **kw):
    return render(request, 'article/index.html')

