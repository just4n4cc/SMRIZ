from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Film
import json
from .forms import FilmForm


def film(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FilmForm()
    return render(request, "film.html", {"form": form})


def films(request):
    data = list(Film.objects.all())

    data_dict = json.loads(serializers.serialize('json', data))
    films_json = [d['fields'] for d in data_dict]
    for i in range(len(data_dict)):
        films_json[i]['id'] = data_dict[i]['pk']
    return HttpResponse(json.dumps(films_json, ensure_ascii=False), content_type='application/json')


def film_by_id(request, pk):
    data = [Film.objects.get(pk=pk)]
    data_dict = json.loads(serializers.serialize('json', data))[0]
    film_json = data_dict['fields']
    film_json['id'] = data_dict['pk']
    return HttpResponse(json.dumps(film_json, ensure_ascii=False), content_type='application/json')
