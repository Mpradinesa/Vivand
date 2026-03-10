from rest_framework import serializers
from .models import Persona, Servicio # Usando tus nombres de modelo

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    # Campos de lectura para facilitar la vida al Frontend
    cuidador_detail = PersonaSerializer(source='cuidador', read_only=True)
    paciente_detail = PersonaSerializer(source='paciente', read_only=True)

    class Meta:
        model = Servicio
        fields = [
            'id', 'cuidador', 'cuidador_detail', 'paciente', 
            'paciente_detail', 'fecha_hora', 'monto_pago', 'estado'
        ]