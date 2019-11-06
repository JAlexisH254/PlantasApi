from django.db import models

# Create your models here.

class Usuario (models.Model):
	nombre_usuario = models.TextField (null = True, blank=True)
	correo_usuario = models.EmailField (null = True, blank=True)
	telefono_usuario = models.TextField (null = True, blank=True)
	contrasenia_usuario = models.CharField (null = True, blank=True, max_length=128)

class Enfermedad (models.Model):
	nombre_enfermedad = models.TextField (null = True, blank=True)
	causa_enfermedad = models.TextField (null = True, blank=True)

class Cultivo (models.Model):
	nombre_cultivo = models.TextField(null = True, blank=True)
	guia_cultivo = models.TextField(null = True, blank=True)
	imagen_cultivo = models.ImageField()
	id_enfermedad = models.ForeignKey(Enfermedad, on_delete = models.CASCADE)
	factor_cultivo = models.FloatField(null = True, blank=True)

class Insumos (models.Model):
	nombre_insumo = models.TextField (null = True, blank=True)
	id_cultivo = models.ForeignKey (Cultivo, on_delete = models.CASCADE)

class Tratamiento (models.Model):
	tratamiento1_tratamiento = models.TextField (null = True, blank=True)		
	tratamiento2_tratamiento = models.TextField (null = True, blank=True)
	tratamiento3_tratamiento = models.TextField (null = True, blank=True)

class Prevencion (models.Model):
	descripcion_prevencion = models.TextField (null = True, blank=True)

class Diagnostico (models.Model):
	id_cultivo=models.ForeignKey(Cultivo,on_delete=models.CASCADE)
	id_enfermedad = models.ForeignKey (Enfermedad, on_delete=models.CASCADE)
	id_tratamiento = models.ForeignKey (Tratamiento, on_delete=models.CASCADE)
	id_prevencion = models.ForeignKey (Prevencion, on_delete=models.CASCADE)

class Historia (models.Model):
	
	fecha_historia=models.DateField()
	coordenaday_historia=models.FloatField()
	coordenadax_historia=models.FloatField()
	id_diagnostico=models.FloatField()

	


