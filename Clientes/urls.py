from django.urls import path, include
from rest_framework import routers
from Clientes import views
from rest_framework.documentation import include_docs_urls

# Generando todas las rutas
router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteView, 'cliente')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Clientes Api')),
    # Solictud de la lista de tipos de documento
    path('api/v1/list_tipo_documento/', views.tipos_documento, name="tipos_documento"),
]