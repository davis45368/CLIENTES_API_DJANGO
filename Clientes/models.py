from django.db import models

class Cliente(models.Model):
    list_tipo_documento = (
        ('CC','Cédula'),
        ('NIT', 'Nit'),
        ('T.I', 'Tarjeta Identidad'),
        ('C.E', 'Cedula Extranjera'),
        ('P', 'Pasaporte')

    )
    nombre_completo = models.CharField(max_length=200)
    numero_documento = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=50, choices=list_tipo_documento, null=True)
    email = models.EmailField(null=True)
    fecha_nacimiento = models.DateField(null=True, default=None)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo