from django.urls import path
from . import views

urlpatterns = [
    path('', views.zwroc_produkty, name='glowna'),
    path('karty_graficzne/', views.zwroc_karty_graficzne, name='karty_graficzne'),
    path('procesory/', views.zwroc_procesory, name='procesory'),
    path('peryferia/', views.zwroc_peryferia, name='peryferia'),
]
