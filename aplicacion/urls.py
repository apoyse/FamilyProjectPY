from django.urls import path

from aplicacion.views import *

urlpatterns =[

    path('inicio/', page,name = 'inicio'),
    path('add/', add ,name = 'add'),


]