from django.shortcuts import render, redirect
from django.views import View
from .forms import ReporteForm

from django.http import HttpResponse

def index(request):

    return HttpResponse("Hola Mundo")

class AgregarReporte(View):
    template_name = "agregar_reporte.html"
    
    def get(self, request):
        form = ReporteForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            print("Formulario válido")
            print("Datos recibidos:", form.cleaned_data)
            form.save()
            print("Guardado exitoso")
            return redirect('index')
        else:
            print("Formulario inválido")
            print("Errores de validación:", form.errors)
        return render(request, self.template_name, {'form': form})
