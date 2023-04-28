from django.contrib import admin
from django.urls import path, include
from clientes.views import clienteviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliente', clienteviewset, basename= 'cliente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
