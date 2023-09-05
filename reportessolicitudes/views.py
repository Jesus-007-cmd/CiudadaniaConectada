from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # Importar el mixin necesario
from .forms import (ReporteForm, 
                    SolicitudForm, 
                    AvanceReporteForm, 
                    AvanceSolicitudForm, 
                    FuncionarioCreationForm, 
                    FuncionarioEditForm  
                    )

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SolicitudInformacion, Open311ReporteProblema, UsuarioFuncionario,AvanceReporte

from django.utils import timezone
from django.contrib import messages
from django.db.models import Count 

from django.db.models.functions import TruncDate
from rest_framework import generics
from .serializers import (
    ReporteProblemaSerializer, 
    SolicitudInformacionSerializer, 
    UsuarioFuncionarioSerializer, 
    AvanceReporteSerializer)

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from django.http import Http404

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


#---------------Aqui inician las vistas de administradores, solo son 2:---------------------
#-------------------------------------------------------------------------------------
@login_required
def admin_home(request):
    template_name = 'admins/admin_home.html'
    
    if request.method == 'POST':
        form = FuncionarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Usuario funcionario creado exitosamente')
                
                return redirect('admin_home')
            except Exception as e:
                messages.error(request, f'Error al crear usuario funcionario: {str(e)}')
                
                print("Error:", e)
    else:
        form = FuncionarioCreationForm()
    
    # Manejo de eliminación de funcionarios
    if request.method == 'POST' and 'eliminar_funcionario' in request.POST:
        funcionario_id = request.POST['eliminar_funcionario']
        try:
            usuario_funcionario = UsuarioFuncionario.objects.get(id=funcionario_id)
            usuario_funcionario.delete()
            messages.success(request, 'Usuario funcionario eliminado exitosamente')
        except UsuarioFuncionario.DoesNotExist:
            messages.error(request, 'El usuario funcionario no existe')
    
    # Manejo de edición de funcionarios
    if request.method == 'POST' and 'editar_funcionario' in request.POST:
        funcionario_id = request.POST['editar_funcionario']
        usuario_funcionario = UsuarioFuncionario.objects.get(id=funcionario_id)
        # Aquí puedes agregar la lógica para cargar el formulario de edición
        
        # Una vez que se haya editado el funcionario, puedes guardar los cambios
        
    funcionarios = UsuarioFuncionario.objects.all()
    
    return render(request, template_name, {'form': form, 'funcionarios': funcionarios})


@login_required
def editar_funcionario(request, funcionario_id):
    funcionario = UsuarioFuncionario.objects.get(id=funcionario_id)

    if request.method == 'POST':
        form = FuncionarioEditForm(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = FuncionarioEditForm(instance=funcionario)

    return render(request, 'admins/editar_funcionario.html', {'form': form, 'funcionario': funcionario})


#---------------Aqui finalizan las vistas de administradores, solo son 2:---------------------

"""Se crean las vistas basadas  en clases para los modelos serializadas """
class ReporteProblemaListView(generics.ListCreateAPIView):
    queryset = Open311ReporteProblema.objects.all()
    serializer_class = ReporteProblemaSerializer

class ReporteProblemaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Open311ReporteProblema.objects.all()
    serializer_class = ReporteProblemaSerializer

class SolicitudInformacionListView(generics.ListCreateAPIView):
    queryset = SolicitudInformacion.objects.all()
    serializer_class = SolicitudInformacionSerializer

class SolicitudInformacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SolicitudInformacion.objects.all()
    serializer_class = SolicitudInformacionSerializer

class UsuarioFuncionarioListView(generics.ListCreateAPIView):
    queryset = UsuarioFuncionario.objects.all()
    serializer_class = UsuarioFuncionarioSerializer

class UsuarioFuncionarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioFuncionario.objects.all()
    serializer_class = UsuarioFuncionarioSerializer

# Vista para listar todos los avances de reporte
class AvanceReporteListaView(generics.ListCreateAPIView):
    queryset = AvanceReporte.objects.all()
    serializer_class = AvanceReporteSerializer

# Vista para ver, actualizar o eliminar un avance de reporte específico
class AvanceReporteDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AvanceReporte.objects.all()
    serializer_class = AvanceReporteSerializer
    
    
 #*/*/*/*/*LO SIGUIENTE PARA OPEN311REPORTEPROBLEMA */*/*/*/*/*/*/*/*/   
    # ListView con get y post
# Vista para listar y crear reportes de problemas
class ReporteProblemaListView(APIView):
    serializer_class = ReporteProblemaSerializer

    # Método para obtener el queryset de los reportes de problemas
    def get_queryset(self):
        return Open311ReporteProblema.objects.all()

    # Método GET para obtener una lista de reportes de problemas
    def get(self, request):
        reportes = self.get_queryset()  # Obtenemos los reportes
        serializer = self.serializer_class(reportes, many=True)  # Serializamos los datos
        return Response(serializer.data)  # Devolvemos la respuesta con los datos serializados

    # Método POST para crear un nuevo reporte de problema
    def post(self, request):
        serializer = self.serializer_class(data=request.data)  # Serializamos los datos recibidos
        if serializer.is_valid():
            serializer.save()  # Si son válidos, guardamos el reporte en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Devolvemos una respuesta con los datos del reporte creado y código 201 (CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Si los datos no son válidos, devolvemos una respuesta de error con detalles de validación y código 400 (BAD REQUEST)

# Vista para ver, actualizar y eliminar un reporte de problema específico
class ReporteProblemaDetailView(APIView):
    serializer_class = ReporteProblemaSerializer

    # Método para obtener un reporte de problema por su clave primaria (ID)
    def get_object(self, pk):
        try:
            return Open311ReporteProblema.objects.get(pk=pk)
        except Open311ReporteProblema.DoesNotExist:
            raise Http404

    # Método GET para obtener los detalles de un reporte de problema por su ID
    def get(self, request, pk):
        reporte_problema = self.get_object(pk)
        serializer = self.serializer_class(reporte_problema)  # Serializamos el reporte
        return Response(serializer.data)  # Devolvemos la respuesta con los detalles serializados

    # Método PUT para actualizar un reporte de problema por su ID
    def put(self, request, pk):
        reporte_problema = self.get_object(pk)
        serializer = self.serializer_class(reporte_problema, data=request.data)  # Serializamos los datos recibidos y los datos actuales del reporte
        if serializer.is_valid():
            serializer.save()  # Si son válidos, guardamos los cambios en el reporte
            return Response(serializer.data)  # Devolvemos una respuesta con los datos actualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Si los datos no son válidos, devolvemos una respuesta de error con detalles de validación y código 400 (BAD REQUEST)

    # Método PATCH para actualizar parcialmente un reporte de problema por su ID
    def patch(self, request, pk):
        reporte_problema = self.get_object(pk)
        serializer = self.serializer_class(reporte_problema, data=request.data, partial=True)  # Serializamos los datos recibidos y los datos actuales del reporte de manera parcial
        if serializer.is_valid():
            serializer.save()  # Si son válidos, guardamos los cambios en el reporte
            return Response(serializer.data)  # Devolvemos una respuesta con los datos actualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Si los datos no son válidos, devolvemos una respuesta de error con detalles de validación y código 400 (BAD REQUEST)

    # Método DELETE para eliminar un reporte de problema por su ID
    def delete(self, request, pk):
        reporte_problema = self.get_object(pk)
        reporte_problema.delete()  # Eliminamos el reporte
        return Response(status=status.HTTP_204_NO_CONTENT)  # Devolvemos una respuesta con código 204 (NO CONTENT) indicando que se ha eliminado
    
#*/*/*/*/*AQUI FINALIZA PARA MODELO OPEN311REPORTEPROBLEMA */*/*/*/*/*/*/*/*/
#*/*/*/*/*LO SIGUIENTE PARA MODELO  SOLICITUDDEINFORMACION */*/*/*/*/*/*/*/*/

# Vista para listar y crear solicitudes de información
class SolicitudInformacionListView(APIView):
    serializer_class = SolicitudInformacionSerializer

    # Método para obtener el queryset de las solicitudes de información
    def get_queryset(self):
        return SolicitudInformacion.objects.all()

    # Método GET para obtener una lista de solicitudes de información
    def get(self, request):
        solicitudes = self.get_queryset()  # Obtenemos las solicitudes
        serializer = self.serializer_class(solicitudes, many=True)  # Serializamos los datos
        return Response(serializer.data)  # Devolvemos la respuesta con los datos serializados

    # Método POST para crear una nueva solicitud de información
    def post(self, request):
        serializer = self.serializer_class(data=request.data)  # Serializamos los datos recibidos
        if serializer.is_valid():
            serializer.save()  # Si son válidos, guardamos la solicitud en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Devolvemos una respuesta con los datos de la solicitud creada y código 201 (CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Si los datos no son válidos, devolvemos una respuesta de error con detalles de validación y código 400 (BAD REQUEST)
    
    
class SolicitudInformacionDetailView(APIView):
        # Obtener un objeto de SolicitudInformacion por su clave primaria (ID)
    def get_object(self, pk):
        try:
            return SolicitudInformacion.objects.get(pk=pk)
        except SolicitudInformacion.DoesNotExist:
            raise Http404

    # Obtener los detalles de una Solicitud de Información por su ID
    def get(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudInformacionSerializer(solicitud)
        return Response(serializer.data)

    # Actualizar una Solicitud de Información por su ID (PUT)
    def put(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudInformacionSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Actualizar parcialmente una Solicitud de Información por su ID (PATCH)
    def patch(self, request, pk):
        solicitud = self.get_object(pk)
        serializer = SolicitudInformacionSerializer(solicitud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar una Solicitud de Información por su ID
    def delete(self, request, pk):
        solicitud = self.get_object(pk)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #*/*/*/*/*FINALIZA LO DE  MODELO  SOLICITUDDEINFORMACION */*/*/*/*/*/*/*/*/
    
    #*/*/*/*/*LO SIGUIENTE PARA MODELO  USUARIOFUNCIONARIO */*/*/*/*/*/*/*/*/
class UsuarioFuncionarioListView(APIView):
    def get(self, request):
        # Obtener todos los usuarios funcionarios con el filtro deseado
        usuarios_funcionarios = UsuarioFuncionario.objects.all()  # Puedes aplicar filtros aquí si es necesario
        serializer = UsuarioFuncionarioSerializer(usuarios_funcionarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioFuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsuarioFuncionarioDetalleView(APIView):
    def get_object(self, pk):
        try:
            return UsuarioFuncionario.objects.get(pk=pk)
        except UsuarioFuncionario.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        usuario_funcionario = self.get_object(pk)
        serializer = UsuarioFuncionarioSerializer(usuario_funcionario)
        return Response(serializer.data)

    def put(self, request, pk):
        usuario_funcionario = self.get_object(pk)
        serializer = UsuarioFuncionarioSerializer(usuario_funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        usuario_funcionario = self.get_object(pk)
        serializer = UsuarioFuncionarioSerializer(usuario_funcionario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuario_funcionario = self.get_object(pk)
        usuario_funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #*/*/*/*/*AQUI FINALIZA PARA MODELO  USUARIOFUNCIONARIO */*/*/*/*/*/*/*/*/
    
    #*/*/*/*/*LO SIGUIENTE PARA MODELO  AVANCE REPORTE */*/*/*/*/*/*/*/*/

class AvanceReporteListaView(APIView):
    def get(self, request):
        avances_reporte = AvanceReporte.objects.all()  # Puedes aplicar filtros aquí si es necesario
        serializer = AvanceReporteSerializer(avances_reporte, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvanceReporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
class AvanceReporteDetalleView(APIView):
    def get_object(self, pk):
        try:
            return AvanceReporte.objects.get(pk=pk)
        except AvanceReporte.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        avance_reporte = self.get_object(pk)
        serializer = AvanceReporteSerializer(avance_reporte)
        return Response(serializer.data)

    def put(self, request, pk):
        avance_reporte = self.get_object(pk)
        serializer = AvanceReporteSerializer(avance_reporte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        avance_reporte = self.get_object(pk)
        serializer = AvanceReporteSerializer(avance_reporte, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        avance_reporte = self.get_object(pk)
        avance_reporte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #*/*/*/*/*AQUI FINALIZA PARA MODELO  AVANCE REPORTE */*/*/*/*/*/*/*/*/