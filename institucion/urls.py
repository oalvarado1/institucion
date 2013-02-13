from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$','escuela.views.ingresar'),
    url(r'^inicio/$','escuela.views.inicio'),
    url(r'^sobre/$','escuela.views.sobre'),
    url(r'^usuarios/$','escuela.views.usuarios'),
    url(r'^usuario/nuevo$','escuela.views.nuevo_usuario'),
    url(r'^universidades/$','escuela.views.lista_universidades'),
    url(r'^universidad/(?P<id_universidad>\d+)$','escuela.views.detalle_universidad'),
    url(r'^contacto/$','escuela.views.contacto'),
    url(r'^comentario/$','escuela.views.comentario'),
    url(r'^universidad/nueva/$','escuela.views.nueva_universidad'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^privado/$','escuela.views.privado'),
    url(r'^cerrar/$','escuela.views.cerrar'),
    
       
)
