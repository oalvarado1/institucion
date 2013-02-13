
from escuela.models import Universidad, Pais, Continente
from escuela.forms import UniversidadForm, PaisForm, ContinenteForm, ContactoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def sobre(request):
	return render_to_response('sobre.html', context_instance=RequestContext(request))

def inicio(request):
    universidades = Universidad.objects.all()
    pais = Pais.objects.all()
    continente = Continente.objects.all()
    return render_to_response('inicio.html',{'universidades':universidades,'pais':pais,'continente':continente}, context_instance=RequestContext(request))
 
def usuarios(request):
    usuarios = User.objects.all()
    universidades = Universidad.objects.all()
    pais = Pais.objects.all()
    continente = Continente.objects.all() 
    return render_to_response('usuarios.html',{'usuarios':usuarios,'universidades':universidades,'pais':pais,'continente':continente}, context_instance=RequestContext(request))

def lista_universidades(request):
    universidades = Universidad.objects.all()
    return render_to_response('universidades.html',{'datos':universidades}, context_instance=RequestContext(request))

def detalle_universidad(request, id_universidad):
    dato = get_object_or_404(Universidad, pk=id_universidad)
    # dato = get_object_or_404(Pais, pk=id_paises)
    # dato = get_object_or_404(Continente, pk=id_continentes)
    return render_to_response('universidad.html',{'universidad':dato},context_instance=RequestContext(request))

def comentario(request):
    return render_to_response('comentario.html',context_instance=RequestContext(request))

def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['oswalvarado@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))

# def comentario(request):

def nueva_universidad(request):
    if request.method=='POST':
        formulario = UniversidadForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/universidades')
    else:
        formulario = UniversidadForm()
    return render_to_response('universidadform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')