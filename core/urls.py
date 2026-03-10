from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from appointments import views  # Importamos las vistas de tu app

urlpatterns = [
    # 1. Administración
    path('admin/', admin.site.urls),
    
    # 2. Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='portada'), name='logout'),
    
    # 3. Páginas del Sistema
    path('', views.portada, name='portada'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('personas/', views.lista_personas, name='lista_personas'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('agenda/', views.agenda, name='agenda'),
    path('api/eventos/', views.calendar_events, name='calendar_events'),
    
    # 4. Creación de Registros (Ruta corregida a persona)
    path('persona/nuevo/', views.crear_persona, name='crear_persona'),
    path('servicio/nuevo/', views.crear_servicio, name='crear_servicio'),
    path('nuevo-turno/', views.nuevo_turno, name='nuevo_turno'),
    
    # 5. Reportes
    path('exportar-excel/', views.exportar_turnos_excel, name='exportar_excel'),
    path('exportar-ficha/', views.exportar_ficha_paciente, name='exportar_ficha_paciente'),
    path('reporte-cuidador/', views.reporte_cuidador_mensual, name='reporte_cuidador'),
    path('reporte-paciente/', views.exportar_turnos_excel, name='reporte_paciente'),
]
