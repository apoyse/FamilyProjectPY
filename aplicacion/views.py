
from django.shortcuts import render
from aplicacion.models import Familiar

def page(request):
    familiares = Familiar.objects.all()
    print(familiares)
    return render(request, 'aplicacion/index.html',{'familiares':familiares})
# Create your views here.
