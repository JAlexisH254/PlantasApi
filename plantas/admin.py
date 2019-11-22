from django.contrib import admin
from plantas.models import *
# Register your models here.

admin.site.register(Afeccion)
admin.site.register(Cultivo)
admin.site.register(Tratamiento)
admin.site.register(Prevencion)
admin.site.register(Diagnostico)
admin.site.register(Usuario)
admin.site.register(UsuarioCultivo)
admin.site.register(CultivoAfeccion)
admin.site.register(TratamientoAfeccion)