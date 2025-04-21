from .views import *
from django.urls import path,include

urlpatterns = [
    path('all/', index, name='index'),
    path('html/', index_html, name='index_html'),
    path('index2/', index2, name='index2'),
    path('rubric/<int:pk>/', detail, name='detail'),
    path('bb/<int:pk>/', detail_bb, name='detail_bb')
]