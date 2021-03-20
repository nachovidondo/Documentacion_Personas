from apps.nuevo.api.serializers.serializers import PersonaSerializer,ProfesionesSerializer
from rest_framework.response import Response
from rest_framework import viewsets

class PersonaViewset(viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = PersonaSerializer.Meta.model.objects.filter(status=True)
    

class ProfesionesViewset(viewsets.ModelViewSet):
    serializer_class = ProfesionesSerializer
    queryset = ProfesionesSerializer.Meta.model.objects.filter(status = True)
    