from django.shortcuts import render
from .models import Article
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import CreateArticle


def index(request):
    articles = Article.objects.all()
    context = {'articles': articles, 'title': 'Home'}
    return render(request, 'index.html', context)


def ViewArticle(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article, 'title': 'View Article'}
    return render(request, 'view_article.html', context)




def createArticle(request):
    if request.method == 'POST':

        form = CreateArticle(request.POST)

        if form.is_valid():
            t = form.cleaned_data['title']
            d = form.cleaned_data['description']
            b = form.cleaned_data['body']
            a = Article(title=t, description=d, body=b)
            a.save()
    else:
        form = CreateArticle()
    context = {'form': form}
    return render(request, 'create.html', context)
