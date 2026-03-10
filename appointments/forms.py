import re
from django import forms
from .models import Turno, Persona, Servicio

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['paciente', 'cuidador', 'servicio', 'titulo', 'inicio', 'fin', 'estado', 'observaciones']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'cuidador': forms.Select(attrs={'class': 'form-select'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Control Mensual - Juan'}),
            'inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'fin': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Notas de la visita...'}),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre', 'apellido', 'rut', 'telefono', 'email', 
            'direccion', 'fecha_nacimiento', 'diagnostico', 'tratamiento_vigente'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12.345.678-K'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle, Número, Comuna'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalle del diagnóstico clínico...'}),
            'tratamiento_vigente': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Medicamentos o terapias actuales...'}),
        }
        
        # CORREGIDO: Ahora está bien cerrado y alineado dentro de Meta
        error_messages = {
            'rut': {
                'unique': "Este RUT ya se encuentra registrado en el sistema.",
                'invalid': "El formato del RUT no es válido.",
            }
        }

    def clean_rut(self):
        """Valida el RUT chileno solo si se ingresó uno."""
        rut = self.cleaned_data.get('rut')
        if not rut:
            return rut
            
        rut_limpio = rut.replace(".", "").replace("-", "").upper().strip()
        
        if not re.match(r"^\d{7,8}[0-9K]$", rut_limpio):
            raise forms.ValidationError("Formato de RUT inválido.")

        cuerpo = rut_limpio[:-1]
        dv = rut_limpio[-1]
        
        suma = 0
        multiplo = 2
        for d in reversed(cuerpo):
            suma += int(d) * multiplo
            multiplo = 2 if multiplo == 7 else multiplo + 1
        
        dv_esperado = str(11 - (suma % 11))
        if dv_esperado == "11": dv_esperado = "0"
        if dv_esperado == "10": dv_esperado = "K"

        if dv != dv_esperado:
            raise forms.ValidationError("El RUT no es válido (dígito verificador incorrecto).")

        return f"{cuerpo}-{dv}"

    def clean_telefono(self):
        """Valida el teléfono solo si el campo no está vacío."""
        telefono = self.cleaned_data.get('telefono')
        
        if not telefono:
            return telefono
            
        tel_limpio = telefono.replace(" ", "").strip()
        
        if not re.match(r"^(\+569|9)\d{8}$", tel_limpio):
            raise forms.ValidationError("El teléfono debe ser +569 o 9 seguido de 8 números.")
        
        if tel_limpio.startswith('9') and len(tel_limpio) == 9:
            tel_limpio = "+56" + tel_limpio
            
        return tel_limpio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'precio', 'descripcion', 'duracion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del servicio'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Breve descripción...'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minutos (ej: 60)'}),
        }
        