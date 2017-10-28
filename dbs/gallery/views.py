from django.shortcuts import render

from django.http import  JsonResponse
from .models import Card


def home(request):

    if request.method == 'POST':
        id_card = request.POST['id_card']
        card = Card.objects.get(id=id_card)
        json_card = {
            'HOLA': 'K ASE?'
        }
        print(request.POST)
        return JsonResponse(json_card)


    template = "home.html"
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, template, context)


def add_image(request):
    template = "agregar.html"
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, template, context)