from django import forms
from .models import Open311ReporteProblema, SolicitudInformacion, AvanceReporte, UsuarioFuncionario
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

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
    finalizar = forms.BooleanField(label="¿Finalizar reporte?", required=False)  # Agrega este campo

    class Meta:
        model = AvanceReporte
        fields = ['comentario', 'finalizar']  # Incluye el campo 'finalizar'

class AvanceSolicitudForm(forms.ModelForm):
    finalizar = forms.BooleanField(label="¿Finalizar solicitud?", required=False)
    
    class Meta:
        model = SolicitudInformacion
        fields = ['comentario', 'finalizar']


#Formulario para crear usuarios funcionarios:
class FuncionarioCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    cargo = forms.CharField(label='Cargo o Puesto', max_length=100)
    departamento = forms.CharField(label='Departamento o Área', max_length=100)
    telefono_contacto = forms.CharField(label='Teléfono de Contacto', max_length=20)
    horario_trabajo = forms.CharField(label='Horario de Trabajo', max_length=100)
    especialidad = forms.CharField(label='Especialidad o Experiencia', max_length=100, required=False)
    foto_perfil = forms.ImageField(label='Foto de Perfil', required=False)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name' ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.is_staff = True  # Asegura que el usuario creado sea un staff
            user.save()
            funcionario = UsuarioFuncionario.objects.create(
                id_funcionario=user,
                cargo=self.cleaned_data['cargo'],
                departamento=self.cleaned_data['departamento'],
                telefono_contacto=self.cleaned_data['telefono_contacto'],
                horario_trabajo=self.cleaned_data['horario_trabajo'],
                especialidad=self.cleaned_data['especialidad'],
                foto_perfil=self.cleaned_data['foto_perfil'],
                
                
            )
        return user
    
class FuncionarioEditForm(forms.ModelForm):
    class Meta:
        model = UsuarioFuncionario
        fields = [
            'cargo',
            'departamento',
            'telefono_contacto',
            'horario_trabajo',
            'especialidad',
            'foto_perfil',
        ]

    def save(self, commit=True):
        funcionario = super().save(commit=False)

        # Elimina la foto existente si se proporciona una nueva imagen
        if 'foto_perfil' in self.changed_data:
            funcionario.foto_perfil.delete(save=False)

        if commit:
            funcionario.save()

        return funcionario