from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect

def index(request):
    
    latest_art_list = Article.objects.order_by('-article_date')[:5]

    return render(request, 'articles/list.html', {'latest_art_list':latest_art_list})
def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Articles not found')
    return render(request, 'articles/detail.html', {'article':a})
def leave_comment(request, article_id):
    pass