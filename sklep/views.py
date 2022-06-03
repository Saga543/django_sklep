from django.shortcuts import render
from .models import Akcesoria
# Create your views here.


def zwroc_produkty(request):
    produkt = Akcesoria.objects.all()
    return render(request, 'sklep_szablony/glowna.html', {'produkty': produkt})
