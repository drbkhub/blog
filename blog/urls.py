from django.urls import path

from blog.views import ArticleListView, ArticleDetailView, UserDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

]
