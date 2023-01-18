from django import template
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from taggit.models import Tag

from .models import Post

# Create your views here.


class HomeView(ListView):

    model = Post
    context_object_name = "posts"
    paginate_by = 7

    def get_template_names(self):

        return "blog/index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
