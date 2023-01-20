from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import CreatePostForm
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


class CreatePostView(CreateView):

    template_name = "blog/create-post.html"
    model = Post
    form_class = CreatePostForm

    def form_valid(self, form):
        if form.is_valid:
            form.save()
        return redirect("homepage")


class EditPostView(UpdateView):

    template_name = "blog/edit-post.html"
    model = Post
    form_class = CreatePostForm
    success_url = reverse_lazy("homepage")
