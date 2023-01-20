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
                attrs={
                    "class": "form-control border-none mt-2 fw-semibold text-capitalize"
                },
            ),
            "subtitle": forms.TextInput(
                attrs={
                    "class": "form-control border-none mt-2 fw-semibold text-capitalize"
                },
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control border-none my-2 fw-semibold text-lowercase"
                },
            ),
            "author": forms.Select(
                attrs={
                    "class": "form-control border-none my-2 form-select fw-semibold text-capitalize"
                },
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control border-none my-2 fw-semibold"},
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-control border-none my-2 form-select fw-semibold"
                },
            ),
            "tags": forms.TextInput(
                attrs={
                    "class": "form-control border-none my-2 mb-2 fw-semibold text-lowercase"
                },
            ),
        }
