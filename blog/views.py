from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Article
from django.contrib.auth.models import User


class ArticleListView(ListView):
    model = Article
    paginate_by = 10  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class ArticleDetailView(DetailView):
    model = Article

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class UserArticlesListView(ListView):
    model = Article
    template_name = 'blog/user_articles_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Article.objects.filter(author__id=self.kwargs.get("pk"))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(pk=self.kwargs.get("pk"))
        return context
