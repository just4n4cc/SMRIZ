import pytest

from django.urls import reverse
from .models import Film
from json import loads


@pytest.mark.django_db
def test_films(client):
    url = reverse('films')
    response = client.get(url)
    assert response.status_code == 200
    json = str(response.json())
    assert json[0] == '[' and json[-1] == ']'


@pytest.mark.django_db
def test_films(client):
    Film.objects.create(title='Test film', description='Test descr', publication_year=2023, genre='thriller')
    url = reverse('film_by_id', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 200
    json = eval(str(response.json()))
    for field in ['title', 'description', 'publication_year', 'genre']:
        assert field in json
