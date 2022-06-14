from django.urls import path

from blog.views import ArticleListView, ArticleDetailView, UserArticlesListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('user/<int:pk>/', UserArticlesListView.as_view(), name='user-articles-list'),

]
