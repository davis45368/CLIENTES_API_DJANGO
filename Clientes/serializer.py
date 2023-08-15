from rest_framework import serializers
from .models import Cliente

#Funcion para covertir los datos a Json y viceversa
class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'