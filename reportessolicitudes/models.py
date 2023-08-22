from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractUser
from django.db import models

#Este permitira guardar los reportes de problemas
class Open311ReporteProblema (models.Model):
    titulo = models.CharField("Título", max_length=300, default="Sin título")
    descripcion = models.TextField("Descripción")
    categoria = models.CharField("Categoría", max_length=100, default="Otra")
    estatus = models.CharField("Estado", max_length=50, default="Pendiente")
    direccion = models.CharField("Ubicación", max_length=200)
    latitud = models.FloatField("Latitud", blank=True, null=True)
    longitud = models.FloatField("Longitud", blank=True, null=True)
    fecha_creacion = models.DateTimeField("Fecha de Creación", auto_now_add=True)
    fecha_ultima_actualizacion = models.DateTimeField("Última Actualización", auto_now=True)
    id_ciudadano = models.CharField('id Ciudadano', max_length=20, unique=True)  
    # Campo para una imagen principal
    imagen = models.ImageField("Imagen", upload_to='reportes_problemas/', blank=True, null=True)
    
    # Campo para múltiples imágenes adicionales
    imagenes = models.ManyToManyField('ImagenReporte', related_name='reportes_problemas')
    archivo_adjunto = models.FileField("Archivo Adjunto", upload_to='archivos_reportes/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class ImagenReporte(models.Model):
    imagen = models.ImageField("Imagen", upload_to='reportes_problemas/')

    def __str__(self):
        return self.imagen.name
    
    

    
 #Aqui se mostraran los avances por fecha de la solicitud si cambia de funcionario o continua el mismo   
class AvanceReporte(models.Model):
    solicitud = models.ForeignKey(Open311ReporteProblema, on_delete=models.CASCADE)
    fecha_avance = models.DateTimeField("Fecha de Avance", auto_now_add=True)
    comentario = models.TextField("Comentario")
    funcionario = models.CharField('id Funcionario', max_length=20, unique=True)
    
#este permitirá guardar las solicitudes de información
class SolicitudInformacion(models.Model):
    titulo = models.CharField("Título", max_length=300, default="Sin título")
    descripcion = models.TextField("Descripción")
    estatus = models.CharField("Estado", max_length=50, default="Pendiente")
    fecha_creacion = models.DateTimeField("Fecha de Creación", auto_now_add=True)
    fecha_ultima_actualizacion = models.DateTimeField("Última Actualización", auto_now=True)
    id_ciudadano = models.CharField('id Ciudadano', max_length=20, unique=True)  
    id_funcionario = models.CharField('id funcionario', max_length=20, unique=True)  
    archivo_adjunto = models.FileField("Archivo Adjunto", upload_to='archivos_solicitudes/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class UsuarioFuncionario(AbstractUser):
    nombres = models.CharField("Nombres", max_length=100)
    apellidos = models.CharField("Apellidos", max_length=100)
    cargo = models.CharField("Cargo o Puesto", max_length=100)
    departamento = models.CharField("Departamento o Área", max_length=100)
    telefono_contacto = models.CharField("Teléfono de Contacto", max_length=20)
    horario_trabajo = models.CharField("Horario de Trabajo", max_length=100)
    especialidad = models.CharField("Especialidad o Experiencia", max_length=100, blank=True)
    foto_perfil = models.ImageField("Foto de Perfil", upload_to='funcionarios/', blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='funcionarios',  # Cambia 'funcionarios' al valor que desees
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='funcionarios',  # Cambia 'funcionarios' al valor que desees
        verbose_name='user permissions'
    )


    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioCiudadano(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='ciudadanos',  # Cambia 'ciudadanos' al valor que desees
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='ciudadanos', 
        verbose_name='user permissions'
    )
    
    def __str__(self):
        return self.username  # O cualquier otro campo que quieras mostrar como representación


class UsuarioAdministrador(AbstractUser):
    class Meta:
        permissions = [
            ("can_do_admin_stuff", "Can do admin stuff"),
            # Agrega más permisos si es necesario
        ]

