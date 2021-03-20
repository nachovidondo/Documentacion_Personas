
from rest_framework import serializers
from apps.nuevo.models import Persona ,Profesiones

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields= '__all__'    
    
class ProfesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesiones
        fields = '__all__'