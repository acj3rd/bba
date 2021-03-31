# TODO: add copyright header

from django.views import View

import logging
import sys
import traceback as tb
from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404
from django.contrib import auth

from betterbay.models import News as NewsDB
from taggit.models import Tag

logger = logging.getLogger(__name__)


def index(request):
    """View function for home page of site."""
    return render(request, 'index.html')


def search(request):
    """View function for searching site. (TODO: just return index for now)"""
    return render(request, 'index.html')

def login(request):
    # if request.user.is_authenticated():
    #     return redirect('admin_page')
    #
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return render(request, 'indexNEW.html')
        else:
            return render(request, 'login2.html', {'messages': ['Error wrong username/password']})

    return render(request, 'login2.html')


class AISView(TemplateView):
    """
    This class handles the display of the AIS page

    By default, it handles GET requests and renders the template based on the attribute "template_name".
    """
    template_name = "ais.html"

    def get(self, *args, **kwargs):
        """
        Handle the GET request for the AIS page
        :param args:
        :param kwargs:
        :return:
        """
        try:
            return render(self.request, self.template_name)

        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            logger.error(tb.format_exception(exc_type, exc_value, exc_tb))


class News(TemplateView):
    """
    This class handles the display of news articles

    By default, it handles GET requests and renders the template based on the attribute "template_name".
    """
    template_name = "news.html"

    def get(self, *args, **kwargs):
        """
        Handle the GET request for the news page
        :param args:
        :param kwargs:
        :return:
        """
        news_articles = NewsDB.objects.all()
        # Show most common tags
        common_tags = NewsDB.tags.most_common()[:4]
        context = {
            'news_articles': news_articles,
            'common_tags': common_tags,
        }
        return render(self.request, 'news.html', context)


def detail_view(request, slug):
    """
    GEt the specific News article
    :param request:
    :param slug:
    :return:
    """
    article = get_object_or_404(NewsDB, slug=slug)
    context = {
        'article': article,
    }
    return render(request, 'news_article.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = News.tags.most_common()[:4]
    articles = News.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'common_tags': common_tags,
        'articles': articles,
    }
    return render(request, 'news.html', context)
