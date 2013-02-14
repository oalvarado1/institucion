
from escuela.models import Universidad, Pais, Continente
from escuela.forms import UniversidadForm, ContactoForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#from django.core import serializers
from django.http import  Http404
from django.utils import simplejson as json

def sobre(request):
	return render_to_response('sobre.html', context_instance=RequestContext(request))

def inicio(request):
    universidades = Universidad.objects.all()
    return render_to_response('inicio.html',{'universidades':universidades}, context_instance=RequestContext(request))
 
def usuarios(request):
    usuarios = User.objects.all()
    universidades = Universidad.objects.all()
    return render_to_response('usuarios.html',{'usuarios':usuarios,'universidades':universidades}, context_instance=RequestContext(request))

def lista_universidades(request):
    universidades = Universidad.objects.all()
    return render_to_response('universidades.html',{'datos':universidades}, context_instance=RequestContext(request))

def detalle_universidad(request, id_universidad):
    dato = get_object_or_404(Universidad, pk=id_universidad)
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

def gestion(request):
    universidades = Universidad.objects.all()
    return render_to_response('index.html',{'universidades':universidades},context_instance=RequestContext(request))

#agregar_universidad
def nueva_universidad(request):
    formulario = UniversidadForm()
    return render_to_response("nueva_universidad.html",{'formulario':formulario},context_instance=RequestContext(request))

#agregar_universidad_ajax
def nueva_universidad_ajax(request):
    if request.is_ajax() and request.method == 'POST':
        formulario = UniversidadForm(request.POST, request.FILES)
        errores = ''
        exito = False
        if formulario.is_valid():
            formulario.save()
            exito = True
        else:
            errores = formulario.errors
        response = {'exito':exito, 'errores':errores}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404

def consulta(request):
    consulta = request.GET.get('q', '') 
    if consulta:         
        results=Universidad.objects.filter(nombre=consulta).order_by('id')
        return render_to_response("inicio.html", { "results": results,"consulta": consulta})  
    return render_to_response("inicio.html", { "results": [],"consulta": consulta})           

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def eliminar(request,id_universidad):
    universidad = Universidad.objects.get(pk=id_universidad)
    universidad.delete()
    return HttpResponseRedirect("/")

def editar(request,id_universidad):
    universidad = Universidad.objects.get(pk=id_universidad)
    formulario = UniversidadForm(instance=universidad)
    return render_to_response("editar_universidad.html",{'formulario':formulario},context_instance=RequestContext(request))

def editar_ajax(request):
    if request.is_ajax() and request.method == 'POST':
        universidad = Universidad.objects.get(pk=request.POST['id_universidad'])
        formulario = UniversidadForm(request.POST, request.FILES, instance=universidad)
        errores = ''
        exito = False
        if formulario.is_valid():
            formulario.save()
            exito = True
        else:
            errores = formulario.errores
        response = {'exito':exito, 'errores':errores}
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        raise Http404

def combo(request):
    query = request.GET.get('q', '') 
    elementos= Pais.objects.all()
    if query:
        results=Universidad.objects.filter(Pais=query)
        return render_to_response("consulta_combo.html",{"results": results,"query": query,"elementos": elementos}, context_instance=RequestContext(request) )
    return render_to_response("consulta_combo.html",{"results": elementos,"query":  query,"elementos": elementos}, context_instance=RequestContext(request))         

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