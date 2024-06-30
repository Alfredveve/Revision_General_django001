from django.shortcuts import render
from . models import Articles
from . forms import ArticlesForm 


def index(request, *args, **kw):
    article = Articles.objects.all()
    
    context = {
        'articles': article
    }
    return render(request, 'article/index.html', context)

def add_article(request):
    messages = ""
    form = ArticlesForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = ArticlesForm()
        messages = "We have successfully created a new article!"
    return render(request, 'article/add.html', {'form': form, 'message': messages})

def table(request):
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'article/table.html', context)


