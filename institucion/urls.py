from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$','escuela.views.inicio'),
    url(r'^ingresar/$','escuela.views.ingresar'),
    url(r'^sobre/$','escuela.views.sobre'),
    url(r'^usuarios/$','escuela.views.usuarios'),
    url(r'^carga/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^usuario/nuevo$','escuela.views.nuevo_usuario'),
    url(r'^universidades/$','escuela.views.lista_universidades'),
    url(r'^universidad/(?P<id_universidad>\d+)$','escuela.views.detalle_universidad'),
    url(r'^gestion/$','escuela.views.gestion'),
    url(r'^contacto/$','escuela.views.contacto'),
    url(r'^comentario/$','escuela.views.comentario'),
    
    # ojo
    # url(r'^universidad/nueva/$','escuela.views.nueva_universidad'),
    
    url(r'^add/$','escuela.views.nueva_universidad'),
    url(r'^add_user_ajax/$','escuela.views.nueva_universidad_ajax'),
    
    url(r'^buscar/$','escuela.views.consulta'),
    url(r'^borrar/(?P<id_universidad>\d+)$','escuela.views.eliminar'),
    url(r'^editar/(?P<id_universidad>\d+)$','escuela.views.editar'),
    url(r'^editar_ajax/$','escuela.views.editar_ajax'),
    url(r'^combo/$','escuela.views.combo'),
    url(r'^privado/$','escuela.views.privado'),
    url(r'^cerrar/$','escuela.views.cerrar'),
)
