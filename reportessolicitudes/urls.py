from django.contrib import admin
from django.urls import path
from . import views

from .views import AgregarReporte


urlpatterns = [
    path('', views.index , name='index'),
    #path('inicio', views.Inicio.as_view(), name='inicio' ),
    
    path('agregar-reporte/', AgregarReporte.as_view(), name='agregar_reporte')

]
