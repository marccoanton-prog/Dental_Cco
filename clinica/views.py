# clinica/views.py
from rest_framework import viewsets
from django.shortcuts import render
from .models import (
    Paciente, 
    Dentista, 
    Cita, 
    TipoDocumento, 
    TipoGenero, 
    EstadoCita, 
    Departamento, 
    Provincia, 
    Distrito, 
    UnidadDental, 
    ProcediDental
)  # Asegúrate de importar los modelos correctos
from .serializers import (
    PacienteSerializer, 
    DentistaSerializer,
    TipoDocumentoSerializer,
    TipoGeneroSerializer,
    EstadoCitaSerializer,
    DepartamentoSerializer,
    ProvinciaSerializer,
    DistritoSerializer,  # Asegúrate de tener un serializer para Distritos
    CitaReadSerializer,
    CitaWriteSerializer,
    UnidadDentalSerializer,
    ProcediDentalSerializer,    
)

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('-pk') # Los últimos agregados saldrán primero
    serializer_class = PacienteSerializer

class DentistaViewSet(viewsets.ModelViewSet):
    queryset = Dentista.objects.all().order_by('-pk')
    serializer_class = DentistaSerializer

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


class UnidadDentalViewSet(viewsets.ModelViewSet):
    queryset = UnidadDental.objects.all().order_by('-pk')
    serializer_class = UnidadDentalSerializer

class ProcediDentalViewSet(viewsets.ModelViewSet):
    queryset = ProcediDental.objects.all().order_by('-pk')
    serializer_class = ProcediDentalSerializer
    

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all().order_by('-fecha_cita', '-hora_cita')

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CitaReadSerializer
        return CitaWriteSerializer