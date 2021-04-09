# TODO: add copyright header

from django.views import View

import logging
import sys
import traceback as tb
from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.apps import apps
from django.db.models import Q

from betterbay.models import News as NewsDB
from taggit.models import Tag

logger = logging.getLogger(__name__)


def index(request):
    """View function for home page of site."""
    return render(request, 'index.html')


def search_demo(request):
    """View function for search demo."""
    return render(request, 'indexModal.html')


def search(request):
    """View function for searching site. (TODO: just return index for now)"""
    return render(request, 'index.html')


def get_news_search(search_term):
    """
    Perform Search on News model
    :param search_term: value to search
    :return:
    """
    return NewsDB.objects.filter(Q(title__contains=search_term) |
                                 Q(author__contains=search_term) |
                                 Q(content__contains=search_term))


def dosearch(request):
    """Handle the POST for search. """
    search_value = request.POST['search_field']

    search_model_results = get_news_search(search_value)
    return render(request, 'search_results.html')


def dosearch_news(request):
    """Handle the POST for search. """
    if 'search_field' in request.POST['search_field']:
        search_value = request.POST['search_field']
    else:
        search_value = ''
    return render(request, 'news.html')


def dosearch_calendar(request):
    """Handle the POST for search. """
    if 'search_field' in request.POST['search_field']:
        search_value = request.POST['search_field']
    else:
        search_value = ''
    return render(request, 'baseCALENDAR.html')


def dosearch_rule(request):
    """Handle the POST for search. """
    if 'search_field' in request.POST['search_field']:
        search_value = request.POST['search_field']
    else:
        search_value = ''
    return render(request, 'rules.html')


def dosearch_about(request):
    """Handle the POST for search. """
    if 'search_field' in request.POST['search_field']:
        search_value = request.POST['search_field']
    else:
        search_value = ''
    return render(request, 'about.html')


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


class Rules(TemplateView):
    """
    This class handles the display of Rules of Road articles

    By default, it handles GET requests and renders the template based on the attribute "template_name".
    """
    template_name = "rules.html"

    def get(self, *args, **kwargs):
        """
        Handle the GET request for the ROR page
        :param args:
        :param kwargs:
        :return:
        """
        try:
            return render(self.request, self.template_name)

        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            logger.error(tb.format_exception(exc_type, exc_value, exc_tb))


class About(TemplateView):
    """
    This class handles the display of About BBA

    By default, it handles GET requests and renders the template based on the attribute "template_name".
    """
    template_name = "about.html"

    def get(self, *args, **kwargs):
        """
        Handle the GET request for the ROR page
        :param args:
        :param kwargs:
        :return:
        """
        try:
            return render(self.request, self.template_name)

        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            logger.error(tb.format_exception(exc_type, exc_value, exc_tb))
