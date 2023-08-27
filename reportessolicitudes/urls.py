from django.contrib import admin
from django.urls import path
from . import views

from .views import AgregarReporte, AgregarSolicitud, IndexUsuarioView


urlpatterns = [
    path('', views.index , name='index'),
    path('agregar-reporte/', AgregarReporte.as_view(), name='agregar_reporte'),
    path('agregar-solicitud/', AgregarSolicitud.as_view(), name='agregar_solicitud'),
    path('index_usuario/', IndexUsuarioView.as_view() , name='index_usuario'),
    path('mis-solicitudes/', views.lista_solicitudes, name='mis_solicitudes'),
    path('mis-reportes/', views.lista_reportes, name='mis_reportes'),
    path('lista_reportes/', views.lista_reportes, name='lista_reportes'),
    path('tomar_solicitud/<int:reporte_id>/', views.tomar_solicitud, name='tomar_solicitud'),
    path('agregar_avance/<int:reporte_id>/', views.agregar_avance, name='agregar_avance'),
]
