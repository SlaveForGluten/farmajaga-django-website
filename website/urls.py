from django.urls import path
from .views import NewsListPL, NewsListEN
from . import views

urlpatterns = [
    path('', views.home_pl, name='farma_jaga-home/pl'),
    path('news/pl/', NewsListPL.as_view(), name='farma_jaga-news/pl'),
    path('contact/pl/', views.contact_pl, name='farma_jaga-contact/pl'),
    path('products/pl/', views.products_pl, name='farma_jaga-products/pl'),


    path('en/', views.home_en, name='farma_jaga-home/en'),
    path('news/en/', NewsListEN.as_view(), name='farma_jaga-news/en'),
    path('contact/en/', views.contact_en, name='farma_jaga-contact/en'),
    path('products/en/', views.products_en, name='farma_jaga-products/en'),



    # path('de/', views.home_de, name='farma_jaga-home/de'),
    # path('news/de/', views.news_de, name='farma_jaga-news/de'),
    # path('contact/de/', views.contact_de, name='farma_jaga-contact/de'),
    # path('products/de/', views.products_de, name='farma_jaga-products/de'),



    # path('sp/', views.home_sp, name='farma_jaga-home/sp'),
    # path('news/sp/', views.news_sp, name='farma_jaga-news/sp'),
    # path('contact/sp/', views.contact_sp, name='farma_jaga-contact/sp'),
    # path('products/sp/', views.products_sp, name='farma_jaga-products/sp'),
]
