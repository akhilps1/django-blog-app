from django import forms

from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = (
            "title",
            "subtitle",
            "slug",
            "author",
            "content",
            "status",
            "tags",
        )

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control border-dark mt-2"},
            ),
            "subtitle": forms.TextInput(
                attrs={"class": "form-control border-dark"},
            ),
            "slug": forms.TextInput(
                attrs={"class": "form-control border-dark"},
            ),
            "author": forms.Select(
                attrs={"class": "form-control border-dark form-select"},
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control border-dark"},
            ),
            "status": forms.Select(
                attrs={"class": "form-control border-dark form-select"},
            ),
            "tags": forms.TextInput(
                attrs={"class": "form-control border-dark mb-2"},
            ),
        }
