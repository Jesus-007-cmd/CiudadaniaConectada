from django.contrib import admin
from django.urls import path
from . import views

from .views import AgregarReporte, AgregarSolicitud, IndexUsuarioView


urlpatterns = [
    
    path('agregar-reporte/', AgregarReporte.as_view(), name='agregar_reporte'),
    path('agregar-solicitud/', AgregarSolicitud.as_view(), name='agregar_solicitud'),
    path('index_usuario/', IndexUsuarioView.as_view() , name='index_usuario'),
    
    path('mis-solicitudes/', views.lista_solicitudes_usuarios, name='mis_solicitudes'),
    path('mis-reportes/', views.lista_reportes, name='mis_reportes'),
    
    #Rutas para funcionario
     path('funcionario/inicio/', views.inicio_funcionario, name='funcionario'),
    path('lista_reportes_funcionario/', views.lista_reportes_funcionario , name='lista_reportes_funcionario'),
    path('funcionario/lista_solicitudes/', views.lista_solicitudes, name='lista_solicitudes_funcionario'),
    path('dar_respuesta_reporte/<int:reporte_id>/', views.dar_respuesta_reportes, name='dar_respuesta'),
    path('dar_respuesta_solicitud/<int:solicitud_id>/', views.dar_respuesta_solicitud, name='dar_respuesta_solicitud'),
    path('reportes/', views.reportes_por_fecha, name='reportes_por_fecha'),
    path('reportes/ciudad/', views.reportes_por_ciudad, name='reportes_por_ciudad'),
    path('reportes/categoria-estatus/', views.reportes_por_categoria_estatus, name='reportes_por_categoria_estatus'),
    #Ruta para admin
    path('admin_home/', views.admin_home, name='admin_home'),
]

