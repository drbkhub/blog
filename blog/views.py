from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Article
from django.contrib.auth.models import User


class ArticleListView(ListView):
    model = Article
    paginate_by = 100  # if pagination is desired

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


class UserDetailView(DetailView):
    model = User
    template_name = 'blog/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(author__id=self.request.user.id)
        return context