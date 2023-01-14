from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Post

# Create your views here.


class HomeView(ListView):

    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 7

    # def get_template_names(self):

    #     if self.request.htmx:
    #         print("XXXXX")
    #     else:
    #         print("None")
    #     return "blog/index.html"
