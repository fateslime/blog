from django.shortcuts import render
from article.models import Article

def article(request):
    articles=Article.objects.all()
    context={'articles':articles}

    return render(request, 'article/article.html',context)
