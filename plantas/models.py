from django.db import models

# Create your models here.
class Tratamiento(models.Model):
	descripcion_tratamiento = models.TextField (null = True, blank=True)

class Afeccion (models.Model):
	nombre_afeccion = models.TextField (null = True, blank=True)
	causa_afeccion = models.TextField (null = True, blank=True)

class Prevencion(models.Model):
	afeccion = models.ForeignKey(Afeccion, on_delete = models.CASCADE)
	descripcion = models.TextField(null =True, blank=True)


class Cultivo (models.Model):
	nombre_cultivo = models.TextField(null = True, blank=True)
	guia_cultivo = models.TextField(null = True, blank=True)
	imagen_cultivo = models.ImageField()
	def __str__(self):
		return self.nombre_cultivo
	

class Usuario (models.Model):
	nombre_usuario = models.TextField (null = True, blank=True)
	correo_usuario = models.EmailField (null = True, blank=True)
	telefono_usuario = models.TextField (null = True, blank=True)
	contrasenia_usuario = models.CharField (null = True, blank=True, max_length=128)
	def __str__(self):
		return self.nombre_usuario
	

class Diagnostico (models.Model):
	afeccion = models.ForeignKey(Afeccion, on_delete = models.CASCADE)
	fecha_diagnostico = models.DateTimeField()
	hora_diagnostico = models.DateField()
	longitud_diagnostico = models.FloatField()
	latitud_diagnostico = models.FloatField()

class UsuarioCultivo (models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	cultivo = models.ForeignKey(Cultivo, on_delete = models.CASCADE)
	diagnostico = models.ForeignKey(Diagnostico, on_delete = models.CASCADE, null = True, blank=True)
	imagen_usuarioCultivo = models.ImageField(null = True, blank=True)
	

class CultivoAfeccion(models.Model):
	cultivo = models.ForeignKey(Cultivo, on_delete = models.CASCADE)
	afeccion = models.ForeignKey(Afeccion, on_delete = models.CASCADE)

class TratamientoAfeccion(models.Model):
	tratamiento = models.ForeignKey(Tratamiento, on_delete = models.CASCADE)
	afeccion = models.ForeignKey(Afeccion, on_delete = models.CASCADE)
