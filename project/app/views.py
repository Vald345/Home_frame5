from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests


data = requests.get('http://api.open-notify.org/iss-now.json')
data = data.json()
print(data)
def index(request):
    s="Список продаж \n\n\n\n\n\n"
    for b in Bd.objects.all():
        s += b.title + "\n" + b.content + "\n\n\n"
    return HttpResponse(s, content_type="text/plain; charset=utf-8")

def index_html(request):
    return render(request, "index.html")
def index2(request):
    return HttpResponse("Bye world")

