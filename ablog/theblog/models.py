from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255, default='other')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    @staticmethod
    def get_absolute_url():
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
