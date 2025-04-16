from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    s="Список продаж \n\n\n\n\n\n"
    for b in Bd.objects.all():
        s += b.title + "\n" + b.content + "\n\n\n"
    return HttpResponse(s, content_type="text/plain; charset=utf-8")

def index_html(request):
    bbs  = Bd.objects.all()
    context = {'bbs': bbs}
    return render(request, 'index.html', context)
def index2(request):
    return HttpResponse("Bye world")

