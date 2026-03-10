from django.db import models

# NOTA: Nunca importes modelos dentro de este mismo archivo, 
# Django ya los reconoce automáticamente aquí.

class Persona(models.Model):
    TIPO_CHOICES = [
        ('PACIENTE', 'Paciente'),
        ('CUIDADOR', 'Cuidador'),
        ('CLIENTE', 'Cliente General'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='PACIENTE')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    
    # CAMPOS PARA LA FICHA MÉDICA PROFESIONAL
    diagnostico = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Diagnóstico Principal"
    )
    tratamiento_vigente = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Tratamientos Activos"
    )
    
    esta_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.get_tipo_display()})"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Turno(models.Model):
    ESTADO_CHOICES = [
        ('PROGRAMADO', 'Programado'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    # Relaciones
    paciente = models.ForeignKey(
        Persona, 
        on_delete=models.CASCADE, 
        limit_choices_to={'tipo': 'PACIENTE'}, 
        related_name='turnos_paciente'
    )
    cuidador = models.ForeignKey(
        Persona, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        limit_choices_to={'tipo': 'CUIDADOR'}, 
        related_name='turnos_cuidador'
    )
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    
    # Datos del Turno
    titulo = models.CharField(max_length=200, help_text="Ej: Control Mensual - Juan")
    inicio = models.DateTimeField(help_text="Fecha y hora de inicio")
    fin = models.DateTimeField(help_text="Fecha y hora de término")
    
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PROGRAMADO')
    color_etiqueta = models.CharField(max_length=7, default='#3788d8', help_text="Color Hex")
    
    # Este campo es vital para el reporte de evolución clínica
    observaciones = models.TextField(
        blank=True, 
        null=True, 
        help_text="Evolución clínica o notas de la visita escribas por el cuidador"
    )

    def __str__(self):
        return f"{self.inicio.strftime('%d/%m %H:%M')} - {self.titulo}"


class ConfiguracionSistema(models.Model):
    nombre_negocio = models.CharField(max_length=100, default="Vivand - Gestión de Cuidados")
    pedir_email = models.BooleanField(default=True)
    pedir_telefono = models.BooleanField(default=True)
    pedir_direccion = models.BooleanField(default=False)
    pedir_fecha_nacimiento = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_negocio