from django.shortcuts import render

from core.models import Cliente
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

