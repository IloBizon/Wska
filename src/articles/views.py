from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Tag, Article, Comment
from django.urls import reverse_lazy
from .forms import CommentForm


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


class CommentUpdateView(FormView):
    model = Comment
    form_class = CommentForm
    template_name = 'article_form.html'
    context_object_name = 'article_form'
    success_url = reverse_lazy('article_detail')


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('article_detail')
