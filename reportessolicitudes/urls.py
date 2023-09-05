from django.contrib import admin
from django.urls import path
from . import views

from .views import (
    AgregarReporte, 
    AgregarSolicitud, 
    IndexUsuarioView,
    ReporteProblemaListView,
    ReporteProblemaDetailView,
    SolicitudInformacionListView,
    SolicitudInformacionDetailView,
    UsuarioFuncionarioListView,
    UsuarioFuncionarioDetalleView,
    AvanceReporteListaView, 
    AvanceReporteDetalleView
)

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
    path('editar-funcionario/<int:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),
    #Rutas serialización
    path('api/reportes-problema/', ReporteProblemaListView.as_view(), name='reportes-problema-lista'),
    path('api/reportes-problema/<int:pk>/', ReporteProblemaDetailView.as_view(), name='reporte-problema-detalle'),
    path('api/solicitudes-informacion/', SolicitudInformacionListView.as_view(), name='solicitudes-informacion-lista'),
    path('api/solicitudes-informacion/<int:pk>/', SolicitudInformacionDetailView.as_view(), name='solicitud-informacion-detalle'),
    path('api/avances-reporte/', AvanceReporteListaView.as_view(), name='avance-reporte-lista'),
    path('api/avances-reporte/<int:pk>/', AvanceReporteDetalleView.as_view(), name='avance-reporte-detalle'),
    path('api/usuarios-funcionario/', UsuarioFuncionarioListView.as_view(), name='usuario-funcionario-lista'),
    path('api/usuarios-funcionario/<int:pk>/', UsuarioFuncionarioDetalleView.as_view(), name='usuario-funcionario-detalle'),

]

