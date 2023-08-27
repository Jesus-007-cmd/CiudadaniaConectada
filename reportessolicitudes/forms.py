from django import forms
from .models import Open311ReporteProblema, SolicitudInformacion, AvanceReporte


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Open311ReporteProblema
        fields = ['titulo', 'descripcion', 'categoria',  'direccion', 'latitud', 'longitud', 'imagen',  'archivo_adjunto']
    

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        descripcion = cleaned_data.get('descripcion')
        categoria = cleaned_data.get('categoria')
        direccion = cleaned_data.get('direccion')
       
        

        if not titulo or not descripcion or not categoria  or not direccion :
            raise forms.ValidationError("Todos los campos deben estar completos")
        return cleaned_data
    

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudInformacion
        fields = ['titulo', 'descripcion',  'archivo_adjunto']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        descripcion = cleaned_data.get('descripcion')
  

        if not titulo or not descripcion  :
            raise forms.ValidationError("Todos los campos deben estar completos")
        return cleaned_data
    
    #Formularios de funcionarios:
    class AvanceReporteForm(forms.ModelForm):
        class Meta:
            model = AvanceReporte
            fields = ['comentario']