from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # Importar el mixin necesario
from .forms import ReporteForm, SolicitudForm

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SolicitudInformacion, Open311ReporteProblema

def index(request):
    return HttpResponse("Hola Mundo")

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

@login_required
def lista_solicitudes(request):
    solicitudes = SolicitudInformacion.objects.filter(id_ciudadano=request.user.id)
    return render(request, 'usuarios/solicitudesdeusuario.html', {'solicitudes': solicitudes})

@login_required
def lista_reportes(request):
    reportes = Open311ReporteProblema.objects.filter(id_ciudadano=request.user.id)
    return render(request, 'usuarios/reportesdeusuario.html', {'reportes': reportes})