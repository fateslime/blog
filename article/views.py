from django.shortcuts import render,redirect
from article.models import Article,Comment
from article.forms import ArticleForm
from django.contrib import messages

def article(request):
    articles={article:Comment.objects.filter(article=article) for article in Article.objects.all()}
    context={'articles':articles}

    return render(request, 'article/article.html',context)
def articleCreate(request):
    template ='article/articleCreate.html'
    if request.method =='GET':  
        return render(request,template,{'articleForm':ArticleForm()})

    articleForm=ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template,{'articleForm':articleForm})

    articleForm.save()
    messages.success(request,'文章已新增')
    return redirect('article:article')


    