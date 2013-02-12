# Create your views here.

from escuela.models import Universidad
# from escuela.forms import RecetaForm, ComentarioForm, ContactoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def sobre(request):
	html = 	html = "<html><body>Proyecto Realizado por: Oswaldo Alvarado Hidalgo & Jonathan Cortez Villa - 2013 </body></html>"
	return HttpResponse(html)

def inicio(request):
    universidades = Universidad.objects.all()
    return render_to_response('inicio.html',{'universidades':universidades}, context_instance=RequestContext(request))

def usuarios(request):
    usuarios = User.objects.all()
    universidades = Universidad.objects.all()
    return render_to_response('usuarios.html',{'usuarios':usuarios,'universidades':universidades}, context_instance=RequestContext(request))

# def lista_univ(request):
#     universidades = Universidad.objects.all()
#     return render_to_response('lista_univ.html',{'lista':universidades})
