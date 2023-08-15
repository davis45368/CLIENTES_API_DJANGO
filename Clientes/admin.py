from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'numero_documento', 'tipo_documento', 'email')
    search_fields = ('id', 'nombre_completo', 'numero_documento', 'email')
    list_filter = ('tipo_documento',)
    list_display_links = ('nombre_completo',)
    list_per_page = 10