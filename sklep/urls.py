from django.urls import path
from . import views

urlpatterns = [
    path('', views.zwroc_produkty, name='glowna'),
]
