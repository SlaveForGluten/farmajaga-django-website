from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home_pl(request):
    return render(request, 'website/pl/home.html')


class NewsListPL(ListView):
    model = Post
    template_name = 'website/pl/news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
