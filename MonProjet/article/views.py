from django.shortcuts import render
from . models import Articles


def index(request, *args, **kw):
    article = Articles.objects.all()
    
    context = {
        'articles': article
    }
    return render(request, 'article/index.html', context)

