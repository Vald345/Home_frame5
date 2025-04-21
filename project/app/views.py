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
    rubrics  = Rubric.objects.all()
    context = {'bbs': bbs, "rubrics": rubrics}
    return render(request, 'index.html', context)
def index2(request):
    return HttpResponse("Bye world")


def detail(request, pk):
    rubric = Rubric.objects.get(pk=pk)
    context = {"rubric": rubric}
    return render(request, 'detail.html', context)


def detail_bb(request, pk):
    bb = Bd.objects.get(pk=pk)
    context = {"bb": bb}
    return render(request, 'detail_bb.html', context)