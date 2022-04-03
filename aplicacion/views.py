from django.http import HttpResponse
from django.shortcuts import render
from aplicacion.models import Familiar

def familares(request):
    return HttpResponse("vista de estudiantes")

def add(request):
    return render(request, 'aplicacion/add.html')

def page(request):
    familiares = Familiar.objects.all()
    return render(request, 'aplicacion/index.html',{'familiares':familiares})
# Create your views here.
