from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from .models import Article
# Create your views here.


def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Sorry, the article you are asking is not exist!")
    context = {}
    context['article_obj'] = article
    return render_to_response("Article.html", context)
    #return render(request, "Article.html", context)
    #return HttpResponse("<h2>articleTitle: %s</h2></br>articleContent: %s" % (article.title,article.content))

def article_list(request):
    articles = Article.objects.all()
    context = {}
    context['articles'] = articles
    return render_to_response("Article_list.html",context)
