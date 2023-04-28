from django.shortcuts import render
from clientes.models import Cliente
from clientes.serializers import clienteSerializer
from rest_framework import serializers, viewsets


class clienteviewset(viewsets.ModelViewSet):
    """exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = clienteSerializer
