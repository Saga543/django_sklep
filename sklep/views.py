from django.shortcuts import render
from .models import Akcesoria
# Create your views here.


def zwroc_produkty(request):
    produkt = Akcesoria.objects.all()
    return render(request, 'sklep_szablony/glowna.html', {'produkty': produkt})


def zwroc_karty_graficzne(request):
    karty_graficzne = Akcesoria.objects.filter(kategoria=1)
    return render(request, 'sklep_szablony/karty_graficzne.html', {'karty_graficzne': karty_graficzne})


def zwroc_procesory(request):
    procesory = Akcesoria.objects.filter(kategoria=2)
    return render(request, 'sklep_szablony/procesory.html', {'procesory': procesory})


def zwroc_peryferia(request):
    peryferia = Akcesoria.objects.filter(kategoria=3)
    return render(request, 'sklep_szablony/peryferia.html', {'peryferia': peryferia})


def koszyk(request):
    return render(request, 'sklep_szablony/koszyk.html', None)
