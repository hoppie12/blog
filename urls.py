from django.urls import path
from .views import ArticleListCreateView, CommentListCreateView

urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:article_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
