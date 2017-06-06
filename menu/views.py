from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Detail
# Create your views here.
def menu(request):
    all_menu = Menu.objects.all()
    return render(request, 'menu/menu.html', {'all_menu' : all_menu})
    #return HttpResponse("<h1>SAHIL</h1>")
def detail(request, menu_id):
    item = Menu.objects.get(id=menu_id)
    return render(request, 'menu/detail.html', {'item' : item} )
