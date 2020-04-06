from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# links to Polish version of the site-------------------------
def home_pl(request):
    return render(request, 'website/pl/home.html', {'title': 'Strona domowa'})


class NewsListPL(ListView):
    model = Post
    template_name = 'website/pl/news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


def contact_pl(request):
    return render(request, 'website/pl/contact.html', {'title': 'Kontakt'})


def products_pl(request):
    return render(request, 'website/pl/products.html', {'title': 'Produkty'})


# English------------------------------------------------------
def home_en(request):
    return render(request, 'website/en/home.html', {'title': 'Home'})


class NewsListEN(ListView):
    model = Post
    template_name = 'website/en/news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


def contact_en(request):
    return render(request, 'website/en/contact.html', {'title': 'Contact'})


def products_en(request):
    return render(request, 'website/en/products.html', {'title': 'Products'})

"""
#German--------------------------------------------------
def home_de(request):
    return render(request, 'website/de/home.html', {'title': 'Home'})


def news_de(request):
    return render(request, 'website/de/news.html', {'title': 'News'})


def contact_de(request):
    return render(request, 'website/de/contact.html', {'title': 'Contact'})


def products_de(request):
    return render(request, 'website/de/products.html', {'title': 'Products'})


#Spanish------------------------------------------------
def home_sp(request):
    return render(request, 'website/sp/home.html', {'title': 'Home'})


def news_sp(request):
    return render(request, 'website/sp/news.html', {'title': 'News'})


def contact_sp(request):
    return render(request, 'website/sp/contact.html', {'title': 'Contact'})


def products_sp(request):
    return render(request, 'website/sp/products.html', {'title': 'Products'})
"""