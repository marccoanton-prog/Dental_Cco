# clinica/views.py
from rest_framework import viewsets
from django.shortcuts import render
from .models import Paciente, Dentista, Cita, TipoDocumento, TipoGenero, EstadoCita 
from .serializers import (
    PacienteSerializer, 
    DentistaSerializer, 
    CitaSerializer,
    TipoDocumentoSerializer,
    TipoGeneroSerializer,
    EstadoCitaSerializer
)

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('-pk') # Los últimos agregados saldrán primero
    serializer_class = PacienteSerializer

class DentistaViewSet(viewsets.ModelViewSet):
    queryset = Dentista.objects.all().order_by('-pk')
    serializer_class = DentistaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all().order_by('fecha_cita', 'hora_cita')
    serializer_class = CitaSerializer

# ViewSets para catálogos (útiles para llenar selectores en los formularios del frontend)
class TipoDocumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoDocumento.objects.filter(activo=True)
    serializer_class = TipoDocumentoSerializer

class TipoGeneroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoGenero.objects.filter(activo=True)
    serializer_class = TipoGeneroSerializer

class EstadoCitaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstadoCita.objects.filter(activo=True)
    serializer_class = EstadoCitaSerializer
