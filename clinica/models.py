from django.db import models
# Create your models here.


# ============================================
# TABLAS DE CATÁLOGO
# ============================================

class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True, db_column='id_tipo_documento')  # Definimos la llave primaria real de tu Postgres
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True, null=True)
    class Meta:
        db_table = 'tipos_documento'
    def __str__(self):
        return self.nombre


class TipoGenero(models.Model):
    id_genero = models.AutoField(primary_key=True, db_column='id_genero')  # Definimos la llave primaria real de tu Postgres
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True, null=True)

    class Meta:
        db_table = 'tipos_genero'
    def __str__(self):
        return self.nombre


class EstadoCita(models.Model):
    id_estado_cita = models.AutoField(primary_key=True, db_column='id_estado_cita')  # Definimos la llave primaria real de tu Postgres
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True, null=True)
    class Meta:
        db_table = 'estados_cita'
    def __str__(self):
        return self.nombre

# ============================================
# TABLAS PRINCIPALES
# ============================================

class Paciente(models.Model):

    id_paciente = models.AutoField(primary_key=True, db_column='id_paciente')  # Definimos la llave primaria real de tu Postgres    
    nombre_primero = models.CharField(max_length=150)
    nombre_segundo = models.CharField(max_length=150, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150, blank=True, null=True)
    id_tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, db_column='id_tipo_documento')
    numero_documento = models.CharField(max_length=20, unique=True, blank=True, null=True)
    correo_pers = models.EmailField(max_length=254, blank=True, null=True)
    correo_corp = models.EmailField(max_length=254, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    telef_fijo = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    id_genero = models.ForeignKey(TipoGenero, on_delete=models.SET_NULL, null=True, db_column='id_genero')

    direccion = models.CharField(max_length=255, blank=True, null=True)
    distrito = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    contacto_emergencia_nombre = models.CharField(max_length=250, blank=True, null=True)
    contacto_emergencia_telefono = models.CharField(max_length=50, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True, null=True)
    class Meta:
        db_table = 'pacientes'
        indexes = [
            models.Index(fields=['numero_documento']),
            models.Index(fields=['correo_pers']),
        ]

    def __str__(self):
        return f"{self.nombre_primero} {self.apellido_paterno}"


class Dentista(models.Model):
    # Definimos la llave primaria real de tu Postgres
    id_dentista = models.AutoField(primary_key=True, db_column='id_dentista')
    # Mapeamos las columnas de tu captura
    nombre_primero = models.CharField(max_length=150)
    nombre_segundo = models.CharField(max_length=150, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150, null=True, blank=True)
    
    # Si tienes una tabla 'tipos_documento', por ahora lo dejamos como entero 
    id_tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, db_column='id_tipo_documento')
    numero_documento = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField(max_length=254, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    telef_fijo = models.CharField(max_length=20, null=True, blank=True)
    numero_colegiado = models.CharField(max_length=50, null=True, blank=True)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)


    class Meta:
        db_table = 'dentistas'
        indexes = [
            models.Index(fields=['numero_documento']),
            models.Index(fields=['numero_colegiado']),
        ]

    def __str__(self):
        segundo = f" {self.nombre_segundo}" if self.nombre_segundo else ""
        return f"Dr(a). {self.nombre_primero}{segundo} {self.apellido_paterno}"


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True, db_column='id_cita')  # Definimos la llave primaria real de tu Postgres
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    dentista = models.ForeignKey(Dentista, on_delete=models.RESTRICT)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    duracion_minutos = models.IntegerField(default=30)
    motivo = models.TextField(blank=True, null=True)

    estado = models.ForeignKey(EstadoCita, on_delete=models.PROTECT, db_column='estado')

    notas = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True, null=True)
    class Meta:
        db_table = 'citas'
    class Meta:
        indexes = [
            models.Index(fields=['paciente']),
            models.Index(fields=['dentista']),
            models.Index(fields=['fecha_cita']),
        ]


class Tratamiento(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    duracion_minutos = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True, null=True)
    class Meta:
        db_table = 'tratamientos'
    def __str__(self):
        return self.nombre