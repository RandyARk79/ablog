from typing import List

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm, EditForm


# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering: List[str] = ['-post_date', '-post_time']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body', )


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # The category page will only one field


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'category_post': category_post})
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'title_tag', 'body',)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
