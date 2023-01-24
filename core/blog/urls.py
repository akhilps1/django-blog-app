from django.urls import path

from . import views

# app_name = "blog"
urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("<slug:post>/", views.post_detail, name="post_detail"),
    path("create-post/", views.CreatePostView.as_view(), name="create_post"),
    path("edit-post/id=<int:pk>/", views.EditPostView.as_view(), name="edit_post"),
    path("delete-post/id=<int:pk>/", views.DeletePost.as_view(), name="delete_post"),
]
