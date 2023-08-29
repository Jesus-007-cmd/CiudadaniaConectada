from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from .forms import RegistroCiudadanoForm, AdminLoginForm
from django.urls import reverse   

def index(request):
    return render(request, 'inicio.html')


def custom_login(request): 
    template_name = 'iniciar_sesion_ciudadano.html'
    
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        User = get_user_model()  # Obtén el modelo de usuario personalizado
       
        # Consulta al usuario usando el modelo personalizado
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        if user is not None:
            if user.is_active:
                # Utiliza el backend de autenticación adecuado
                login(request, user)
                print('--------------> Si entró al login')
                return redirect('/reportessolicitudes/index_usuario/')
            else:
                print('----------------> Usuario no activo')
                messages.error(request, 'El usuario no está activo')
        else:
            print('----------------> Credenciales inválidas')
            messages.error(request, 'Credenciales inválidas')
    return render(request, template_name)

def custom_logout(request):
    logout(request)
    return redirect(reverse('index'))

def register(request):
    if request.method == 'POST':   
        form = RegistroCiudadanoForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('index_usuario')  # Redirige primero
            user = authenticate(username=username, password=password)
            login(request, user)  # Luego autentica al usuario
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en {field}: {error}')
    else:
        form = RegistroCiudadanoForm()
    return render(request, 'registration/register.html', {'form': form})

# Aqui empieza login de usuariofuncionario:
def es_funcionario(user):
    return hasattr(user, 'usuariofuncionario')

def login_funcionario_view(request):
    template_name = "iniciar_sesion_funcionario.html"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and es_funcionario(user):
            login(request, user)
            return redirect('funcionario')
        else:
            messages.error(request, 'Credenciales inválidas para funcionario')
    
    return render(request, template_name)

# Aqui empieza de adminsitrador:
def admin_login(request):
    template_name = 'iniciar_sesion_admin.html'
    
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_home')  # Cambia 'admin_home' por la URL a la página de administrador
            else:
                messages.error(request, 'Credenciales inválidas o no tienes permisos de administrador')
    else:
        form = AdminLoginForm()
    
    return render(request, template_name, {'form': form})







