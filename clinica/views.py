# clinica/views.py
from rest_framework import viewsets
from django.shortcuts import render
from .models import Paciente, Dentista, Citas, TipoDocumento, TipoGenero, EstadoCita, Departamento, Provincia, Distrito
from .serializers import (
    PacienteSerializer, 
    DentistaSerializer, 
    CitasSerializer,
    TipoDocumentoSerializer,
    TipoGeneroSerializer,
    EstadoCitaSerializer,
    DepartamentoSerializer,
    ProvinciaSerializer,
    DistritoSerializer  # Asegúrate de tener un serializer para Distritos
)

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('-pk') # Los últimos agregados saldrán primero
    serializer_class = PacienteSerializer

class DentistaViewSet(viewsets.ModelViewSet):
    queryset = Dentista.objects.all().order_by('-pk')
    serializer_class = DentistaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all().order_by('-pk')
    serializer_class = CitasSerializer

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

class DepartamentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Departamento.objects.all().order_by('nombre')
    serializer_class = DepartamentoSerializer

class ProvinciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Provincia.objects.all().order_by('nombre')
    serializer_class = ProvinciaSerializer  

class DistritoViewSet(viewsets.ModelViewSet):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer