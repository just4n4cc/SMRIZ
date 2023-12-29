from django.db import models


class Film(models.Model):
    # title = models.CharField(max_length=250, name='Название')
    # description = models.TextField(name='Описание')
    # pub_year = models.IntegerField(name='Год выпуска', null=False, blank=False)
    # genre = models.CharField(name='Жанр', max_length=50, null=False, blank=False)

    title = models.CharField(max_length=250)
    description = models.TextField()
    publication_year = models.IntegerField(null=False, blank=False)
    genre = models.CharField(max_length=50, null=False, blank=False)
