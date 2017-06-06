from django.shortcuts import render
from django.http import HttpResponse
from .models import Map_location

def home(request):
    
    return render(request, 'home/home.html')
    #return HttpResponse("<h1>SAHIL</h1>")
    
def find(request):
    map = Map_location.objects.get(id=1)
    return render(request, 'home/find.html', {'map':map})


def sahil(request):
    return render(request, 'home/sahil.html')