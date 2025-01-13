from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Tag, Article, Comment
from django.urls import reverse_lazy
from .forms import CommentForm
from django.contrib.auth.models import User

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles.html'


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail.html'


class CommentCreateView(FormView):
    model = Comment
    form_class = CommentForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('article_detail')

    def form_valid(self, form):
        pk=self.kwargs['pk']
        user = self.request.user
        article = Article.objects.get(id=pk)
        Comment.objects.create(
            text = self.request.POST.get('text'),
            article=article,
            user=user
        )
        return redirect('article_detail', pk)


class CommentUpdateView(FormView):
    model = Comment
    form_class = CommentForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('article_detail')

    def form_valid(self, form):
        pk=self.kwargs['pk']
        user = self.request.user
        article = Article.objects.get(id=pk)
        comment_id = self.kwargs['id']
        comment = Comment.objects.filter(id=comment_id)
        comment.update(
            text = self.request.POST.get('text'),
            article=article,
            user=user
        )
        return redirect('article_detail', pk)

