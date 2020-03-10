from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Article

from django.http import HttpResponse

import platform
import sys


#
# def index(request):
#     return HttpResponse("Привет, мир!")
#
def test(request):
    return HttpResponse("ТЕСТОВАЯ СТРАНИЦА")


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    latest_comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def leave(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    text = 'platform.uname(): {} \n sys.version: {} \n platform.architecture(): {}'.format(platform.uname(),
                                                                                           sys.version,
                                                                                           platform.architecture())
    a.comment_set.create(author_name='', comment_text=text)

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
