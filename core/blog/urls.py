from django.urls import path

from . import views

# app_name = "blog"
urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("post-id=<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("create-post/", views.CreatePostView.as_view(), name="create_post"),
]
