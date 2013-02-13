#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Continente(models.Model):
	nombre_cont = models.CharField(max_length=50, verbose_name='Continente', unique=True)
	area_cont = models.CharField(max_length=50, verbose_name='Área', unique=True)
	poblacion_cont = models.CharField(max_length=50, verbose_name='Población', unique=True)
	Usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre_cont

class Pais(models.Model):
	Continente = models.ForeignKey(Continente)
	nombre_pais = models.CharField(max_length=50, verbose_name='País', unique=True)
	capital_pais = models.CharField(max_length=50, verbose_name='Capital', unique=True)
	lengua_pais = models.CharField(max_length=50, verbose_name='Idioma', unique=True)
	moneda_pais = models.CharField(max_length=50, verbose_name='Moneda', unique=True)
	Usuario = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.nombre_pais

class Universidad(models.Model):
	Continente = models.ForeignKey(Continente)
	Pais = models.ForeignKey(Pais)
	nombre_univ = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
	categoria_univ = models.CharField(max_length=100, verbose_name='Categoria', unique=True)
	pagina_web_univ = models.CharField(max_length=50, verbose_name='URL', unique=True)
	Usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre_univ

