from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout




    
def custom_login(request): #kwards validacion de varios argumentos pero solo se accedera al puro metodo
    template_name='login.html'
    if request.method == 'POST':  #dos parametros se requieren para aceder al login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print('--------------> Si entró al login')
            return redirect('/libros/inicio/')
        else:
            print('----------------> No entró al login')
            messages.error(request, 'Credenciales inválidas') 
    return render(request, template_name)

def custom_logout(request):
    logout(request) #se le pasa nuestro request que incluira toda la información para generar el logout
    return redirect('/login/')

def register(request):
    if request.method == 'POST':   
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('inicio')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})