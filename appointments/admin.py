from django.contrib import admin
from .models import Persona, Servicio, Turno, ConfiguracionSistema

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'tipo', 'esta_activo')
    list_filter = ('tipo', 'esta_activo')
    search_fields = ('nombre', 'apellido', 'rut')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'precio')
    search_fields = ('nombre',)

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    # Usamos los nuevos campos del "Súper Turno"
    list_display = ('inicio', 'titulo', 'paciente', 'cuidador', 'estado')
    list_filter = ('estado', 'inicio', 'cuidador')
    date_hierarchy = 'inicio'
    search_fields = ('titulo', 'paciente__nombre', 'cuidador__nombre')
    # Esto hace que el selector de fecha y hora sea más cómodo en el admin
    filter_horizontal = () 

@admin.register(ConfiguracionSistema)
class ConfiguracionSistemaAdmin(admin.ModelAdmin):
    list_display = ('nombre_negocio',)