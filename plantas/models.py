from django.db import models

# Create your models here.

class Usuario (models.model):
	nombre_usuario = models.TextField (null = True, blank=True)
	correo_usuario = models.EmailField (null = True, blank=True)
	telefono_usuario = models.TextField (null = True, blank=True)
	contrasenia_usuario = models.CharField (null = True, blank=True, max_length=128)

class Cultivo (models.model):
	nombre_cultivo = models.TextField(null = True, blank=True)
	guia_cultivo = models.TextField(null = True, blank=True)
	imagen_cultivo = models.ImageField()
	id_enfermedad = models.ForeignKey(Enfermedad, on_delete = models.CASCADE)
	factor_cultivo = models.Floatfield(null = True, blank=True)

class Insumos (models.model):
	nombre_insumo = models.TextField (null = True, blank=True)
	id_cultivo = models.ForeignKey (Cultivo, on_delete = models.CASCADE)


class Diagnostico (models.model):
	id_enfermedad = models.ForeignKey (Enfermedad, on_delete=models.CASCADE)
	id_solucion = models.ForeignKey (Solucion, on_delete=models.CASCADE)
	id_tratamiento = models.ForeignKey (Tratamiento, on_delete=models.CASCADE)
	id_prevencion = models.ForeignKey (Prevencion, on_delete=models.CASCADE)

class Tratamiento (models.model):
	tratamiento1_tratamiento = models.TextField (null = True, blank=True)		
	tratamiento2_tratamiento = models.TextField (null = True, blank=True)
	tratamiento3_tratamiento = models.TextField (null = True, blank=True)
	
class Prevencion (models.model):
	descripcion_prevencion = models.TextField (null = True, blank=True)

class Enfermedad (models.model):
	nombre_enfermedad = models.TextField (null = True, blank=True)
	causa_enfermedad = models.TextField (null = True, blank=True)
