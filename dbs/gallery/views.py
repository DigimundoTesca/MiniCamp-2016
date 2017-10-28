from django.shortcuts import render
from .models import Card


def home(request):
    template = "home.html"
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, template, context)

