#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Universidad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    continente = models.CharField(max_length=50, verbose_name='Continente', unique=True)
    pais = models.CharField(max_length=50, verbose_name='País', unique=True)
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad', unique=True)
    idioma = models.CharField(max_length=50, verbose_name='Idioma', unique=True)
    url = models.CharField(max_length=50, verbose_name='URL', unique=True)
    def __unicode__(self):
        return self.nombre