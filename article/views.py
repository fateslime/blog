from django.shortcuts import render,redirect,get_object_or_404
from article.models import Article,Comment
from article.forms import ArticleForm
from django.contrib import messages
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required
from main.views import admin_required


def article(request):
    articles={article:Comment.objects.filter(article=article) for article in Article.objects.all()}
    context={'articles':articles}

    return render(request, 'article/article.html',context)

@login_required
def articleCreate(request):
    template = 'article/articleCreateUpdate.html'
    if request.method =='GET':  
        return render(request,template,{'articleForm':ArticleForm()})

    articleForm=ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template,{'articleForm':articleForm})

    articleForm.save()
    messages.success(request,'文章已新增')
    return redirect('article:article')


def articleRead(request, articleId):
	article = get_object_or_404(Article, id=articleId)
	context = {
		'article': article,
		'comments': Comment.objects.filter(article=article)
	}
	return render(request, 'article/articleRead.html', context)

@login_required
def articleUpdate(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=article)
        return render(request, template, {'articleForm':articleForm})

    articleForm = ArticleForm(request.POST, instance=article)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})

    articleForm.save()
    messages.success(request, '文章已修改') 
    return redirect('article:articleRead', articleId=articleId)

@admin_required
def articleDelete(request, articleId):
    '''
    Delete the article instance:
        1. Render the article page if the method is GET
        2. Get the article to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return redirect('article:article')

    # POST
    article = get_object_or_404(Article, id=articleId)
    article.delete()
    messages.success(request, '文章已刪除')  
    return redirect('article:article')

    