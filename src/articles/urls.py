from django.urls import path
from .views import ArticleListView, ArticleDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/comments/create', CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/comments/<int:id>/update', CommentUpdateView.as_view(), name='comment_update'),
    path('<int:pk>/comments/<int:id>/delete', CommentDeleteView.as_view(), name='comment_delete'),
]
