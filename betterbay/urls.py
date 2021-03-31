# TODO: Add copyright header
from django.conf.urls import url
from django.urls import path
from . import views
from . import views_swingtime

urlpatterns = [
    path('', views.index, name='index'),
    path(r'ais/', views.AISView.as_view()),
    url(r'^events/$', views_swingtime.event_listing, name='bba-events'),
    url(r'^events/add/$', views_swingtime.add_event, name='bba-add-event'),
    url(r'^events/(\d+)/$', views_swingtime.event_view, name='bba-event'),
    url(r'^events/(\d+)/(\d+)/$', views_swingtime.occurrence_view, name='bba-occurrence'),
    url(r'^calendar/$', views_swingtime.today_view, name='bba-today'),
    url(r'^calendar/(?P<year>\d{4})/$', views_swingtime.year_view, name='bba-yearly-view'),
    url(
        r'^calendar/(\d{4})/(0?[1-9]|1[012])/$',
        views_swingtime.month_view,
        name='bba-monthly-view'
    ),
    url(r'^calendar/(\d{4})/(0?[1-9]|1[012])/([0-3]?\d)/$',
        views_swingtime.day_view,
        name='bba-daily-view'),
    url(r'^news', views.News.as_view(), name='bba-news'),
    path('^news_article/<slug:slug>/', views.detail_view, name="detail"),
    path('^news_tag/<slug:slug>/', views.tagged, name="tagged"),

    url(r'^login/$', views.login, name='bba-login'),
    url(r'^search/$', views.search, name='bba-search')
]
