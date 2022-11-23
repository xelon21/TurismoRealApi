# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articulo(models.Model):
    id_articulo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descirpcion = models.CharField(max_length=30)
    costo_reposicion = models.BigIntegerField()
    fehca_actualizacion = models.DateField()
    id_categoria = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'articulo'


class Categoria(models.Model):
    id_categoria = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Departamento(models.Model):
    id_depto = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=550)
    valor_noche = models.BigIntegerField()
    id_zona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='id_zona')
    m2 = models.BigIntegerField()
    imagen_url = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    capacidad = models.BigIntegerField()
    q_banos = models.BigIntegerField()
    q_plazas = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'departamento'


class DetHuesped(models.Model):
    id_huesped = models.OneToOneField('Huesped', models.DO_NOTHING, db_column='id_huesped', primary_key=True)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')

    class Meta:
        managed = False
        db_table = 'det_huesped'
        unique_together = (('id_huesped', 'id_reserva'),)


class DetInventario(models.Model):
    id_det = models.BigAutoField(primary_key=True)
    id_articulo = models.ForeignKey('Articulo', models.DO_NOTHING, db_column='id_articulo')
    id_inventario = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='id_inventario')

    class Meta:
        managed = False
        db_table = 'det_inventario'       


class DetPg(models.Model):
    id_reserva = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='id_reserva', primary_key=True)
    id_pg = models.ForeignKey('PagoGasto', models.DO_NOTHING, db_column='id_pg')

    class Meta:
        managed = False
        db_table = 'det_pg'
        unique_together = (('id_reserva', 'id_pg'),)


class DetServicio(models.Model):
    id_servicio = models.OneToOneField('ServicioExtra', models.DO_NOTHING, db_column='id_servicio', primary_key=True)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')

    class Meta:
        managed = False
        db_table = 'det_servicio'
        unique_together = (('id_servicio', 'id_reserva'),)


class DispServ(models.Model):
    id_servicio = models.OneToOneField('ServicioExtra', models.DO_NOTHING, db_column='id_servicio', primary_key=True)
    id_zona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='id_zona')

    class Meta:
        managed = False
        db_table = 'disp_serv'
        unique_together = (('id_servicio', 'id_zona'),)


class Empleado(models.Model):
    id_empleado = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey ('Usuario', models.DO_NOTHING, db_column='id_usuario')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    id_zona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='id_zona')
    tipo_empleado = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'empleado'


class EncargadoProc(models.Model):
    id_empleado = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='id_empleado', primary_key=True)
    id_tipo_proc = models.ForeignKey('TipoProc', models.DO_NOTHING, db_column='id_tipo_proc')
    id_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='id_estado')
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')

    class Meta:
        managed = False
        db_table = 'encargado_proc'


class Estado(models.Model):
    id_estado = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado'


class GastoDepto(models.Model):
    id_gasto =  models.BigAutoField(primary_key=True)
    id_depto = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='id_depto')
    id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='id_empleado')
    id_medio_pago = models.ForeignKey('MedioPago', models.DO_NOTHING, db_column='id_medio_pago')
    concepto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    valor_pago = models.BigIntegerField()
    fecha_pago = models.DateField()

    class Meta:
        managed = False
        db_table = 'gasto_depto'


class Huesped(models.Model):
    id_huesped = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    rut = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huesped'


class Inventario(models.Model):
    id_inventario = models.BigAutoField(primary_key=True)
    id_depto = models.BigIntegerField()
    fecha_actualiz = models.DateField()

    class Meta:
        managed = False
        db_table = 'inventario'

class MedioPago(models.Model):
    id_mp = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'medio_pago'

class PagoGasto(models.Model):
    id_pg = models.BigAutoField(primary_key=True)
    concepto = models.CharField(max_length=30)
    descirpcion = models.CharField(max_length=30, blank=True, null=True)
    fecha_pago = models.DateField()
    id_medio_pago = models.ForeignKey(MedioPago, models.DO_NOTHING, db_column='id_medio_pago')
    monto = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pago_gasto'

class Reserva(models.Model):
    id_reserva = models.BigAutoField(primary_key=True)
    f_checkin = models.DateField()
    f_checkout = models.DateField()
    id_huesped = models.ForeignKey(Huesped, models.DO_NOTHING, db_column='id_huesped')
    valor_reserva = models.BigIntegerField()
    valor_total = models.BigIntegerField()
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado')
    id_depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_depto')

    class Meta:
        managed = False
        db_table = 'reserva'

class ServicioExtra(models.Model):
    id_servicio = models.BigAutoField(primary_key=True)
    id_tipo_serv = models.BigIntegerField()
    tarifa = models.BigIntegerField()
    fecha_pago = models.DateField()

    class Meta:
        managed = False
        db_table = 'servicio_extra'

class TipoProc(models.Model):
    id_tipo = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_proc'

class TipoServ(models.Model):
    id_tipo = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_serv'

class TipoUsuario(models.Model):
    id_tipo = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'

class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=30)
    contrasena = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=100, blank=True, null=True)
    rut = models.CharField(max_length=12, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'usuario'

class Zona(models.Model):
    id_zona = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'zona'
