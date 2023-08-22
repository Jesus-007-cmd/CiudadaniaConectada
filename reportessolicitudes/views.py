from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'inicio.html'
    def post(self, request):

        return
    
    def get(self, request):
        '''
        Esta es mi clase get
        '''
        print('Ya inicio mi GET -------*')

        return render(request, self.template_name)