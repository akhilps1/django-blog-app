import pytest
from django.urls import reverse

from core.blog.models import Post

pytestmark = pytest.mark.django_db


class TestHomePage:
    def test_home_page(self, client):
        url = reverse("homepage")
        response = client.get(url)

        assert response.status_code == 200
