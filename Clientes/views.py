from .models import Cliente
from .serializer import ClientesSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Renderizar toda la lista de CLientes en formato Json
class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClientesSerializer
    queryset = Cliente.objects.all()

#Renderizar Lista de tipo de docuemento
@api_view(['GET'])
def tipos_documento(request):
    
    TIPOS_DOCUMENTO = Cliente.list_tipo_documento
    
    return Response(TIPOS_DOCUMENTO)