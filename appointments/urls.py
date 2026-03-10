from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, ServicioViewSet
from . import views

# Configuración de la API (para el calendario u otras integraciones)
router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'servicios', ServicioViewSet)

urlpatterns = [
    # Dashboard Principal
    path('', views.dashboard, name='dashboard'),
    
    # Rutas para los nuevos formularios (Estilo el de la imagen)
    path('paciente/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('servicio/nuevo/', views.crear_servicio, name='crear_servicio'),

    # Rutas para listas (si las necesitas aparte)
    path('personas/lista/', views.lista_personas, name='lista_personas'),
    path('servicios/lista/', views.lista_servicios, name='lista_servicios'),
    
    # API y Calendario
    path('api/', include(router.urls)),
    path('api/eventos/', views.calendar_events, name='calendar_events'),
    
    # Reporte Excel
    path('exportar-ficha/', views.exportar_ficha_paciente, name='exportar_ficha_paciente'),
]