from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "web/home.html"
    context_object_name = "posts"
    ordering = ["-data_posted"]
