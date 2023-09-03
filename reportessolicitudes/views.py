from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # Importar el mixin necesario
from .forms import ReporteForm, SolicitudForm, AvanceReporteForm, AvanceSolicitudForm, FuncionarioCreationForm

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SolicitudInformacion, Open311ReporteProblema, UsuarioFuncionario

from django.utils import timezone
from django.contrib import messages
from django.db.models import Count 

from django.db.models.functions import TruncDate

# Inician Vistas de usuario
class IndexUsuarioView(LoginRequiredMixin, View):
    template_name = "usuarios/index.html"

    def get(self, request):
        return render(request, self.template_name)

class AgregarReporte(LoginRequiredMixin, View):
    template_name = "usuarios/agregar_reporte.html"

    def get(self, request):
        form = ReporteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            print("Formulario válido")
            print("Datos recibidos:", form.cleaned_data)
            print("Guardado exitoso")
            reporte = form.save(commit=False)
            reporte.id_ciudadano = request.user.id  # Agregar el identificador del usuario
            reporte.save()
            return redirect('index_usuario')
        else:
            print("Formulario inválido")
            print("Errores de validación:", form.errors)
        return render(request, self.template_name, {'form': form})

class AgregarSolicitud(LoginRequiredMixin, View):
    template_name = "usuarios/agregar_solicitud.html"

    def get(self, request):
        form = SolicitudForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            print("Formulario válido")
            print("Datos recibidos:", form.cleaned_data)
            solicitud = form.save(commit=False)
            solicitud.id_ciudadano = request.user.id  # Agregar el identificador del usuario
            solicitud.save()
            print("Guardado exitoso")
            return redirect('index_usuario')
        else:
            print("Formulario inválido")
            print("Errores de validación:", form.errors)
        return render(request, self.template_name, {'form': form})
# Terminan vistas de usuario

def lista_solicitudes_usuarios(request):
    if request.user.is_authenticated:
        solicitudes = SolicitudInformacion.objects.filter(id_ciudadano=request.user.id)
        return render(request, 'usuarios/solicitudesdeusuario.html', {'solicitudes': solicitudes})
    else:
        # Manejar el caso cuando el usuario no está autenticado
        return redirect('index_usuario')

def lista_reportes(request):
    if request.user.is_authenticated:
        
        reportes = Open311ReporteProblema.objects.filter(id_ciudadano=request.user.id)
        return render(request, 'usuarios/reportesdeusuario.html', {'reportes': reportes})
    else:
        # Manejar el caso cuando el usuario no está autenticado
        return redirect('index_usuario')

#-------------------------------------------------------------------------------------
#---------------De aqui adelante estan las vistas de funcionarios:---------------------
#esta función permitira evaluar si el usuario es funcionario antes de entrar a una vista
def es_funcionario(user):
    return hasattr(user, 'usuariofuncionario')


@user_passes_test(es_funcionario)
def inicio_funcionario(request):
    return render(request, 'funcionarios/inicio_funcionario.html')
    
@user_passes_test(es_funcionario)
def lista_reportes_funcionario(request):
    reportes_funcionario = Open311ReporteProblema.objects.all()
    return render(request, 'funcionarios/lista_reportes_funcionario.html', {'reportes': reportes_funcionario})

@user_passes_test(es_funcionario)
def dar_respuesta_reportes(request, reporte_id):
    reporte = get_object_or_404(Open311ReporteProblema, pk=reporte_id)
   
    if request.method == 'POST':
        avance_form = AvanceReporteForm(request.POST)
        if avance_form.is_valid():
            avance = avance_form.save(commit=False)
            avance.solicitud = reporte
            avance.funcionario = request.user
            avance.save()
            reporte.fecha_ultima_actualizacion = timezone.now()
            reporte.save()
            if avance_form.cleaned_data['finalizar']:  # Verifica si el campo 'finalizar' está marcado
                reporte.estatus = 'Finalizado'
                reporte.save()

            return redirect('lista_reportes_funcionario')

    else:
        avance_form = AvanceReporteForm()

    return render(request, 'funcionarios/dar_respuesta_reportes.html', {'reporte': reporte, 'avance_form': avance_form})

@user_passes_test(es_funcionario)
def lista_solicitudes(request):
    solicitud = SolicitudInformacion.objects.all()
    return render(request, 'funcionarios/lista_solicitudes.html', {'solicitudes': solicitud})

@user_passes_test(es_funcionario)
def dar_respuesta_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudInformacion, pk=solicitud_id)

    if request.method == 'POST':
        avance_form = AvanceSolicitudForm(request.POST)
        if avance_form.is_valid():
            avance = avance_form.save(commit=False)
            avance.solicitud = solicitud
            avance.save()
            solicitud.estatus = 'Finalizado'
            solicitud.save()

            return redirect('lista_solicitudes_funcionario')  # Cambiar a la URL correcta

    else:
        avance_form = AvanceSolicitudForm()

    return render(request, 'funcionarios/dar_respuesta_solicitud.html', {'solicitud': solicitud, 'avance_form': avance_form})



@user_passes_test(es_funcionario)
def reportes_por_fecha(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        # Consulta para contar los reportes por día
        reportes_por_dia_finalizados = Open311ReporteProblema.objects.filter(
            fecha_creacion__range=(start_date, end_date), estatus='Finalizado')
        reportes_por_dia_pendientes = Open311ReporteProblema.objects.filter(
            fecha_creacion__range=(start_date, end_date), estatus='Pendiente')
        reportes_grafico_finalizados = reportes_por_dia_finalizados.annotate(
            fecha_dia=TruncDate('fecha_creacion')
        ).values('fecha_dia').annotate(
            total_reportes=Count('id')
        ).order_by('fecha_dia')
        reportes_grafico_pendientes = reportes_por_dia_pendientes.annotate(
            fecha_dia=TruncDate('fecha_creacion')
        ).values('fecha_dia').annotate(
            total_reportes=Count('id')
        ).order_by('fecha_dia')
        
        # Preparar datos para el gráfico
        labels_finalizados = [entry['fecha_dia'].strftime('%Y-%m-%d') for 
                              entry in reportes_grafico_finalizados]
        data_finalizados = [entry['total_reportes'] for entry in 
                            reportes_grafico_finalizados]
        labels_pendientes = [entry['fecha_dia'].strftime('%Y-%m-%d') for 
                             entry in reportes_grafico_pendientes]
        data_pendientes = [entry['total_reportes'] for entry in 
                           reportes_grafico_pendientes]
        
        
        return render(request, 'funcionarios/reportes_por_fecha.html', 
                      {'labels_finalizados': labels_finalizados, 'data_finalizados': 
                       data_finalizados, 'reportes_por_dia_finalizados': 
                       reportes_por_dia_finalizados, 'labels_pendientes': 
                       labels_pendientes, 'data_pendientes': data_pendientes, 
                       'reportes_por_dia_pendientes': reportes_por_dia_pendientes})
    
    

@user_passes_test(es_funcionario)
def reportes_por_ciudad(request):
    ciudad = request.GET.get('ciudad')
    
    reportes = Open311ReporteProblema.objects.filter(direccion__icontains=ciudad).order_by('titulo')
    
    return render(request, 'funcionarios/reportes.html', {'reportes': reportes})

@user_passes_test(es_funcionario)
def reportes_por_categoria_estatus(request):
    categoria = request.GET.get('categoria')
    estatus = request.GET.get('estatus')
    
    reportes = Open311ReporteProblema.objects.filter(categoria=categoria, estatus=estatus)
    
    return render(request, 'funcionarios/reportes.html', {'reportes': reportes})



#---------------Hasta aqui finalizan las vistas de funcionarios:---------------------
#-------------------------------------------------------------------------------------





@login_required
def admin_home(request):
    template_name = 'admins/admin_home.html'
    
    if request.method == 'POST':
        form = FuncionarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()  # Guarda el usuario
                
                #funcionario.save()  # Guarda el registro de UsuarioFuncionario
                messages.success(request, 'Usuario funcionario creado exitosamente')
                
                print(user.id)
                return redirect('admin_home')  # Redirige nuevamente a la página de administrador
            except Exception as e:
                messages.error(request, f'Error al crear usuario funcionario: {str(e)}')
                print("Error:", e)

    else:
        form = FuncionarioCreationForm()
    
    
    funcionarios = UsuarioFuncionario.objects.all()  # Obtén la lista de funcionarios existentes
    
    return render(request, template_name, {'form': form, 'funcionarios': funcionarios})