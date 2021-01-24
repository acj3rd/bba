# TODO: Add copyright header

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'ais/', views.AISView.as_view()),
]
