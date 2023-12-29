from django.http import HttpResponse
from markdown import markdown


def index(request):
    with open('../README.md') as f:
        readme = f.read()
        html = markdown(readme)
        return HttpResponse(html)
