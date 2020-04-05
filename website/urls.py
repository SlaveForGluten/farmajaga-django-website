from django.urls import path
from .views import NewsListPL  #NewsListEN
from . import views

urlpatterns = [
    path('', views.home_pl, name='website-home/pl'),
    path('news/pl/', NewsListPL.as_view(), name='website-news/pl'),
]