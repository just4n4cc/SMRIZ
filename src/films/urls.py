from django.urls import path

from . import views

urlpatterns = [
    path('films', views.films, name='films'),
    path('films/<int:pk>', views.film_by_id, name='film_by_id'),
    path("", views.film, name="film"),
]
