from django.urls import path
from . import views

urlpatterns = [
    path('', views.zwroc_produkty, name='glowna'),
    path('karty_graficzne/', views.zwroc_karty_graficzne, name='karty_graficzne'),
]
