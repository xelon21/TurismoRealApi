import json
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from core.models import Zona, Departamento, Articulo, Categoria, Empleado, Usuario, TipoUsuario, GastoDepto, MedioPago, Estado, Huesped, Reserva
from core.models import DetInventario, Inventario, MedioPago, ServicioExtra, TipoServ, DispServ

from django.db import connection


def ingreso_departamentos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()  #este llama
    out_cursor = django_cursor.connection.cursor() #este recibe

    cursor.callproc('SP_INGRESADEPARTAMENTOS', [])

def listado_departamentos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor(Departamento())

    cursor.callproc('SP_LISTARDEPARTAMENTOS', [out_cursor])

    lista = [Departamento]
    for fila in out_cursor:
        lista.append(fila)
    
    return lista

#class PostApiViewSet(ModelViewSet):
    #serializer_class= PostSerializer
   # queryset = Zona.objects.all()

#class DepartamentosViewSet(ModelViewSet):
 #   serializer_class=DepartamentoSerializer
  #  queryset = Departamento.objects.all()

class ZonaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            zonas = list(Zona.objects.filter(id_zona=id).values())
            if len(zonas) > 0:
                zona = zonas[0]
                datos = {'Zona': zona}
            else:
                datos = {'message': "No se encontraron zonas"}
            return JsonResponse(datos)
        else:
            zonas = list(Zona.objects.values())
            if len(zonas) > 0:
                datos = {'Zona': zonas}
                datosOrdenados = {'Zona' : (sorted(datos["Zona"],key=lambda d: d["id_zona"]))}
            else:
                datos = {'message': "No se encontraron zonas"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        Zona.objects.create(descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        zonas = list(Zona.objects.filter(id_zona=id).values())
        if len(zonas) > 0:
            zona = Zona.objects.get(id_zona = id)
            zona.descripcion = jd['descripcion']
            zona.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron zonas"}
        return JsonResponse(datos)
    def delete(self,request, id):
        zonas = list(Zona.objects.filter(id_zona = id).values())
        if len(zonas) > 0:
            Zona.objects.filter(id_zona=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron zonas"}
        return JsonResponse(datos)

class DepartamentoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            departamentos = list(Departamento.objects.filter(id_depto=id).values())
            if len(departamentos) > 0:
                departamento = departamentos[0]
                print (departamento)
                datos = {'Departamento': departamento}
            else:
                datos = {'message': "No se encontraron departamentos"}
            return JsonResponse(datos)
        else:
            departamentos = list(Departamento.objects.values())
            if len(departamentos) > 0:
                #lstDeptos = departamentos.sort()
                datos = {'Departamento': departamentos} #.sort(key=lambda x: x['id_depto'])}#, reverse=True)}
                datosOrdenados = {'Departamento' : (sorted(datos["Departamento"],key=lambda d: d["id_depto"]))}
                #deptoOrdenado = sorted(datos.items)
            else:
                datos = {'message': "No se encontraron departamentos"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        print(jd)
        zona = Zona.objects.get(id_zona=jd['id_zona_id'])   
        Departamento.objects.create(descripcion=jd['descripcion'], valor_noche=jd['valor_noche'], id_zona=zona,
                                     m2=jd['m2'], imagen_url=jd['imagen_url'], direccion=jd['direccion'], capacidad=jd['capacidad'],
                                     q_banos=jd['q_banos'], q_plazas=jd['q_plazas'])            
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        departamentos = list(Departamento.objects.filter(id_depto=id).values())
        if len(departamentos) > 0:
            id_zona=jd['id_zona']
            zona = Zona.objects.get(id_zona=id_zona) 
            departamento = Departamento.objects.get(id_depto = id)
            departamento.descripcion = jd['descripcion']
            departamento.valor_noche = jd['valor_noche']
            departamento.id_zona = zona
            departamento.m2 = jd['m2']
            departamento.imagen_url = jd['imagen_url']
            departamento.direccion = jd['direccion']
            departamento.capacidad = jd['capacidad']
            departamento.q_banos = jd['q_banos']
            departamento.q_plazas = jd['q_plazas']
            departamento.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron departamentos"}
        return JsonResponse(datos)
    def delete(self,request, id):
        departamentos = list(Departamento.objects.filter(id_depto = id).values())
        if len(departamentos) > 0:
            Departamento.objects.filter(id_zona=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron departamentos"}
        return JsonResponse(datos)

class ArticuloView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            articulos = list(Articulo.objects.filter(id_articulo=id).values())
            if len(articulos) > 0:
                articulo = articulos
                datos = {'Articulo': articulo}
            else:
                datos = {'message': "No se enconto el articulo"}
            return JsonResponse(datos)
        else:
            articulos = list(Articulo.objects.values())
            if len(articulos) > 0:
                datos = {'articulos': articulos}
                datosOrdenados = {'articulos' : (sorted(datos["articulos"],key=lambda d: d["id_articulo"]))}
            else:
                datos = {'message': "No se encontraron articulos"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        print(jd)
        #categoria = Categoria.objects.get(id_categoria = jd['id_categoria'])
        Articulo.objects.create(nombre=jd['nombre'], descirpcion=jd['descirpcion'], 
                                costo_reposicion=jd['costo_reposicion'], 
                                fehca_actualizacion=jd['fehca_actualizacion'],
                                id_categoria=jd['id_categoria'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        articulos = list(Articulo.objects.filter(id_articulo=id).values())
        if len(articulos) > 0:
            articulo = Articulo.objects.get(id_articulo = id)
            articulo.nombre = jd['nombre']
            articulo.descirpcion = jd['descirpcion']
            articulo.costo_reposicion = jd['costo_reposicion']
            articulo.fehca_actualizacion = jd['fehca_actualizacion']
            articulo.id_categoria = jd['id_categoria']
            articulo.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron articulos"}
        return JsonResponse(datos)
    def delete(self,request, id):
        articulos = list(Articulo.objects.filter(id_articulo = id).values())
        if len(articulos) > 0:
            Articulo.objects.filter(id_articulo=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron articulos"}
        return JsonResponse(datos)

class CategoriaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            categorias = list(Categoria.objects.filter(id_categoria=id).values())
            if len(categorias) > 0:
                categoria = categorias[0]
                datos = {'categorias': categoria}
            else:
                datos = {'message': "No se encontraron categorias"}
            return JsonResponse(datos)
        else:
            categorias = list(Categoria.objects.values())
            if len(categorias) > 0:
                datos = {'categorias': categorias}
                datosOrdenados = {'categorias' : (sorted(datos["categorias"],key=lambda d: d["id_categoria"]))}
            else:
                datos = {'message': "No se encontraron categorias"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        print("entro")
        Categoria.objects.create(descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        categorias = list(Categoria.objects.filter(id_categoria=id).values())
        if len(categorias) > 0:
            categoria = Categoria.objects.get(id_categoria = id)
            categoria.descripcion = jd['descripcion']
            categoria.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron categorias"}
        return JsonResponse(datos)
    def delete(self,request, id):
        categorias = list(Categoria.objects.filter(id_categoria = id).values())
        if len(categorias) > 0:
            Categoria.objects.filter(id_categoria=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron categorias"}
        return JsonResponse(datos)

class EmpleadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            empleados = list(Empleado.objects.filter(id_empleado=id).values())
            if len(empleados) > 0:
                empleado = empleados[0]
                datos = {'empleados': empleado}
            else:
                datos = {'message': "No se encontraron empleados"}
            return JsonResponse(datos)
        else:
            empleados = list(Empleado.objects.values())
            if len(empleados) > 0:
                datos = {'empleados': empleados}
                datosOrdenados = {'empleados' : (sorted(datos["empleados"],key=lambda d: d["id_empleado"]))}
            else:
                datos = {'message': "No se encontraron empleados"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        print(jd)
        id_usuario = Usuario.objects.get(id_usuario=jd['id_usuario_id']) 
        zona = Zona.objects.get(id_zona=jd['id_zona_id']) 
        Empleado.objects.create(id_usuario=id_usuario, nombre=jd['nombre'],
                                apellido=jd['apellido'], rut=jd['rut'],
                                direccion=jd['direccion'], id_zona=zona,
                                tipo_empleado=jd['tipo_empleado'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        empleados = list(Empleado.objects.filter(id_empleado=id).values())
        if len(empleados) > 0:
            id_usuario = Usuario.objects.get(id_usuario=jd['id_usuario']) 
            zona = Zona.objects.get(id_zona=jd['id_zona']) 
            empleado = Empleado.objects.get(id_empleado = id)
            empleado.id_usuario = id_usuario
            empleado.nombre = jd['nombre']
            empleado.apellido = jd['apellido']
            empleado.rut = jd['rut']
            empleado.direccion = jd['direccion']
            empleado.id_zona = zona
            empleado.tipo_empleado = jd['tipo_empleado']
            empleado.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron empleados"}
        return JsonResponse(datos)
    def delete(self,request, id):
        empleados = list(Empleado.objects.filter(id_empleado = id).values())
        if len(empleados) > 0:
            Empleado.objects.filter(id_empleado=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron empleados"}
        return JsonResponse(datos)

class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            usuarios = list(Usuario.objects.filter(id_usuario=id).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'usuarios': usuario}
            else:
                datos = {'message': "No se encontraron usuarios"}
            return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'usuarios': usuarios}
                datosOrdenados = {'usuarios' : (sorted(datos["usuarios"],key=lambda d: d["id_usuario"]))}
            else:
                datos = {'message': "No se encontraron usuarios"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        print(jd)
        id_tipo = TipoUsuario.objects.get(id_tipo=jd['id_tipo_usuario_id'])         
        Usuario.objects.create(email=jd['email'], contrasena=jd['contrasena'],
                               nombre_completo=jd['nombre_completo'], rut=jd['rut'],
                               direccion=jd['direccion'], telefono=jd['telefono'],
                               fecha_nacimiento=jd['fecha_nacimiento'], id_tipo_usuario=id_tipo)
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id_usuario=id).values())
        if len(usuarios) > 0:
            id_tipo = TipoUsuario.objects.get(id_tipo=jd['id_tipo_usuario_id'])    
            usuario = Usuario.objects.get(id_usuario = id)
            usuario.email = jd['email']
            usuario.contrasena =jd['contrasena']
            usuario.nombre_completo = jd['nombre_completo']
            usuario.rut = jd['rut']
            usuario.direccion= jd['direccion']
            usuario.telefono = jd['telefono']
            usuario.fecha_nacimiento = jd['fecha_nacimiento']
            usuario.id_tipo_usuario = id_tipo
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron usuarios"}
        return JsonResponse(datos)
    def delete(self,request, id):
        usuarios = list(Usuario.objects.filter(id_usuario = id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id_usuario=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron usuarios"}
        return JsonResponse(datos)

class TipoUsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            tipoUsuarios = list(TipoUsuario.objects.filter(id_tipo=id).values())
            if len(tipoUsuarios) > 0:
                tipoUsuario = tipoUsuarios[0]
                datos = {'tipoUsuario': tipoUsuario}
            else:
                datos = {'message': "No se encontraron tipoUsuarios"}
            return JsonResponse(datos)
        else:
            tipoUsuarios = list(TipoUsuario.objects.values())
            if len(tipoUsuarios) > 0:
                datos = {'tipoUsuario': tipoUsuarios}
                datosOrdenados = {'tipoUsuario' : (sorted(datos["tipoUsuario"],key=lambda d: d["id_tipo"]))}
            else:
                datos = {'message': "No se encontraron tipoUsuarios"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        TipoUsuario.objects.create(descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        tipoUsuarios = list(TipoUsuario.objects.filter(id_tipo=id).values())
        if len(tipoUsuarios) > 0:
            tipoUsuario = TipoUsuario.objects.get(id_tipo = id)
            tipoUsuario.descripcion = jd['descripcion']
            tipoUsuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron tipoUsuarios"}
        return JsonResponse(datos)
    def delete(self,request, id):
        tipoUsuarios = list(TipoUsuario.objects.filter(id_tipo = id).values())
        if len(tipoUsuarios) > 0:
            TipoUsuario.objects.filter(id_tipo=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron tipoUsuarios"}
        return JsonResponse(datos)

class GastoDeptoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            gastoDeptos = list(GastoDepto.objects.filter(id_gasto=id).values())
            if len(gastoDeptos) > 0:
                gastoDepto = gastoDeptos[0]
                datos = {'gastoDeptos': gastoDepto}
            else:
                datos = {'message': "No se encontraron gastoDeptos"}
            return JsonResponse(datos)
        else:
            gastoDeptos = list(GastoDepto.objects.values())
            if len(gastoDeptos) > 0:
                datos = {'gastoDeptos': gastoDeptos}
                datosOrdenados = {'gastoDeptos' : (sorted(datos["gastoDeptos"],key=lambda d: d["id_gasto"]))}
            else:
                datos = {'message': "No se encontraron gastoDeptos"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        departamento = Departamento.objects.get(id_depto=jd['id_depto_id'])
        empleado = Empleado.objects.get(id_empleado= jd['id_empleado_id'])
        medioPago = MedioPago.objects.get(id_mp=jd['id_medio_pago_id']) 
        GastoDepto.objects.create(id_depto=departamento, id_empleado=empleado, id_medio_pago=medioPago,
                            concepto=jd['concepto'], descripcion=jd['descripcion'], valor_pago=jd['valor_pago'],
                            fecha_pago=jd['fecha_pago'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        gastoDeptos = list(GastoDepto.objects.filter(id_gasto=id).values())
        if len(gastoDeptos) > 0:
            departamento = Departamento.objects.get(id_depto=jd['id_depto'])
            empleado = Empleado.objects.get(id_empleado= jd['id_empleado'])
            medioPago = MedioPago.objects.get(id_medio_pago=jd['id_medio_pago']) 
            gastoDepto = GastoDepto.objects.get(id_gasto = id)
            gastoDepto.id_depto = departamento
            gastoDepto.id_empleado = empleado
            gastoDepto.id_medio_pago = medioPago
            gastoDepto.concepto = jd['concepto']
            gastoDepto.descripcion = jd['descripcion']
            gastoDepto.valor_pago = jd['valor_pago']
            gastoDepto.fecha_pago = jd['fecha_pago']
            gastoDepto.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron gastoDeptos"}
        return JsonResponse(datos)
    def delete(self,request, id):
        gastoDeptos = list(GastoDepto.objects.filter(id_gasto = id).values())
        if len(gastoDeptos) > 0:
            GastoDepto.objects.filter(id_gasto=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron gastoDeptos"}
        return JsonResponse(datos)

class EstadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            estados = list(Estado.objects.filter(id_estado=id).values())
            if len(estados) > 0:
                estado = estados[0]
                datos = {'estados': estado}
            else:
                datos = {'message': "No se encontraron estados"}
            return JsonResponse(datos)
        else:
            estados = list(Estado.objects.values())
            if len(estados) > 0:
                datos = {'estados': estados}
                datosOrdenados = {'estados' : (sorted(datos["estados"],key=lambda d: d["id_estado"]))}
            else:
                datos = {'message': "No se encontraron estados"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        Estado.objects.create(descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        estados = list(Estado.objects.filter(id_estado=id).values())
        if len(estados) > 0:
            estado = Estado.objects.get(id_estado = id)
            estado.descripcion = jd['descripcion']
            estado.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron estados"}
        return JsonResponse(datos)
    def delete(self,request, id):
        estados = list(Estado.objects.filter(id_estado = id).values())
        if len(estados) > 0:
            Estado.objects.filter(id_estado=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron estados"}
        return JsonResponse(datos)

class HuespedView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            huespedes = list(Huesped.objects.filter(id_huesped=id).values())
            if len(huespedes) > 0:
                huesped = huespedes[0]
                datos = {'huesped': huesped}
            else:
                datos = {'message': "No se encontraron huespedes"}
            return JsonResponse(datos)
        else:
            huespedes = list(Huesped.objects.values())
            if len(huespedes) > 0:
                datos = {'huesped': huespedes}             
                datos2 = {'huesped' : (sorted(datos["huesped"],key=lambda d: d["id_huesped"]))}                        
            else:
                datos = {'message': "No se encontraron huespedes"}
            return JsonResponse(datos2)
    def post(self,request):
        jd = json.loads(request.body)
        usuario = Usuario.objects.get(id_usuario=jd['id_usuario'])   
        Huesped.objects.create(nombre=jd['nombre'], apellido=jd['apellido'], rut=['rut'],
                               direccion=jd['direccion'], telefono=jd['telefono'], id_usuario=usuario)
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        huespedes = list(Huesped.objects.filter(id_huesped=id).values())
        if len(huespedes) > 0:
            usuario = Usuario.objects.get(id_usuario=jd['id_usuario'])   
            huesped = Huesped.objects.get(id_huesped = id)
            huesped.nombre = jd['nombre']
            huesped.apellido = jd['apellido']
            huesped.rut = jd['rut']
            huesped.direccion = jd['direccion']
            huesped.telefono = jd['telefono']
            huesped.id_usuario = usuario
            huesped.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron huespedes"}
        return JsonResponse(datos)
    def delete(self,request, id):
        huespedes = list(Huesped.objects.filter(id_huesped = id).values())
        if len(huespedes) > 0:
            Huesped.objects.filter(id_huesped=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron huespedes"}
        return JsonResponse(datos)

class ReservaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            reservas = list(Reserva.objects.filter(id_reserva=id).values())
            if len(reservas) > 0:
                reserva = reservas[0]
                datos = {'reservas': reserva}
            else:
                datos = {'message': "No se encontraron reservas"}
            return JsonResponse(datos)
        else:
            reservas = list(Reserva.objects.values())
            if len(reservas) > 0:
                datos = {'reservas': reservas}                
                datosOrdenados = {'reservas' : (sorted(datos["reservas"],key=lambda d: d["id_reserva"]))}                
            else:
                datos = {'message': "No se encontraron reservas"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        print(jd)
        huesped = Huesped.objects.get(id_huesped=jd['id_huesped'])  
        estado = Estado.objects.get(id_estado=jd['id_estado'])  
        depto = Departamento.objects.get(id_depto=jd['id_depto']) 
        Reserva.objects.create(f_checkin=jd['f_checkin'], f_checkout=jd['f_checkout'], id_huesped=huesped, 
                               valor_reserva=jd['valor_reserva'], valor_total=jd['valor_total'],
                               id_estado=estado, id_depto=depto)
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self,request, id):
        jd = json.loads(request.body)
        reservas = list(Reserva.objects.filter(id_reserva=id).values())
        if len(reservas) > 0:
            huesped = Huesped.objects.get(id_huesped=jd['id_huesped'])  
            estado = Estado.objects.get(id_estado=jd['id_estado'])  
            depto = Departamento.objects.get(id_depto=jd['id_depto']) 
            reserva = Reserva.objects.get(id_reserva = id)
            reserva.f_checkin = jd['f_checkin']
            reserva.f_checkout = jd['f_checkout']
            reserva.id_huesped = huesped
            reserva.valor_reserva = jd['valor_reserva']
            reserva.valor_total = jd['valor_total']
            reserva.id_estado = estado
            reserva.id_depto = depto
            reserva.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron reservas"}
        return JsonResponse(datos)
    def delete(self,request, id):
        reservas = list(Reserva.objects.filter(id_reserva = id).values())
        if len(reservas) > 0:
            Reserva.objects.filter(id_reserva=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encontraron reservas"}
        return JsonResponse(datos)

class DetalleInventarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            detInventarios = list(DetInventario.objects.filter(id_det=id).values())
            if len(detInventarios) > 0:
                detInventario = detInventarios[0]
                datos = {'detalleInventario': detInventario}
            else:
                datos = {'message': "No se encontraron datos"}
            return JsonResponse(datos)
        else:
            detInventarios = list(DetInventario.objects.values())
            if len(detInventarios) > 0:
                datos = {'detalleInventario': detInventarios}
                datosOrdenados = {'detalleInventario' : (sorted(datos["detalleInventario"],key=lambda d: d["id_det"]))}
            else:
                datos = {'message': "No se encontraron datos"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        articulo = Articulo.objects.get(id_articulo=jd['id_articulo_id'])  
        inventario = Inventario.objects.get(id_inventario=jd['id_inventario_id'])
        DetInventario.objects.create(id_articulo=articulo, id_inventario=inventario)
        datos = {'message': "Success"}
        return JsonResponse(datos)  

class InventarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            inventarios = list(Inventario.objects.filter(id_inventario=id).values())
            if len(inventarios) > 0:
                inventario = inventarios[0]
                datos = {'inventarios': inventario}
            else:
                datos = {'message': "No se encontraron inventarios"}
            return JsonResponse(datos)
        else:
            inventarios = list(Inventario.objects.values())
            if len(inventarios) > 0:
                datos = {'inventarios': inventarios}
                datosOrdenados = {'inventarios' : (sorted(datos["inventarios"],key=lambda d: d["id_inventario"]))}
            else:
                datos = {'message': "No se encontraron inventarios"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
     #   depto = Departamento.objects.get(id_depto=jd['id_depto']) 
        Inventario.objects.create(id_depto=jd['id_depto'], fecha_actualiz=jd['fecha_actualiz'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

class MedioPagoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            medioPagos = list(MedioPago.objects.filter(id_mp=id).values())
            if len(medioPagos) > 0:
                medioPago = medioPagos[0]
                datos = {'medioPagos': medioPago}
            else:
                datos = {'message': "No se encontraron medioPagos"}
            return JsonResponse(datos)
        else:
            medioPagos = list(MedioPago.objects.values())
            if len(medioPagos) > 0:
                datos = {'medioPagos': medioPagos}
                datosOrdenados = {'medioPagos' : (sorted(datos["medioPagos"],key=lambda d: d["id_mp"]))}
            else:
                datos = {'message': "No se encontraron medioPagos"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        MedioPago.objects.create(descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)   

class ServicioExtraView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            servicioExtras = list(ServicioExtra.objects.filter(id_servicio=id).values())
            if len(servicioExtras) > 0:
                servicioExtra = servicioExtras[0]
                datos = {'servicioExtras': servicioExtra}
            else:
                datos = {'message': "No se encontraron servicios extras"}
            return JsonResponse(datos)
        else:
            servicioExtras = list(ServicioExtra.objects.values())
            if len(servicioExtras) > 0:
                datos = {'servicioExtras': servicioExtras}
                datosOrdenados = {'servicioExtras' : (sorted(datos["servicioExtras"],key=lambda d: d["id_servicio"]))}
            else:
                datos = {'message': "No se encontraron servicios extras"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)       
        ServicioExtra.objects.create( id_tipo_serv=jd['id_tipo_serv'], tarifa=jd['tarifa'], fecha_pago=jd['fecha_pago'])
        datos = {'message': "Success"}
        return JsonResponse(datos)   

class TipoServicioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            tipoServicios = list(TipoServ.objects.filter(id_tipo=id).values())
            if len(tipoServicios) > 0:
                tipoServicio = tipoServicios[0]
                datos = {'tipoServicios': tipoServicio}
            else:
                datos = {'message': "No se encontraron Tipos Servicios"}
            return JsonResponse(datos)
        else:
            tipoServicios = list(TipoServ.objects.values())
            if len(tipoServicios) > 0:
                datos = {'tipoServicios': tipoServicios}
                datosOrdenados = {'tipoServicios' : (sorted(datos["tipoServicios"],key=lambda d: d["id_tipo"]))}
            else:
                datos = {'message': "No se encontraron Tipos Servicios"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body)
        TipoServ.objects.create(descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

class DispServView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            dispServs = list(DispServ.objects.filter(id_disp_serv=id).values())
            if len(dispServs) > 0:
                dispServ = dispServs[0]
                datos = {'dispServs': dispServ}
            else:
                datos = {'message': "No se encontraron dispServs"}
            return JsonResponse(datos)
        else:
            dispServs = list(DispServ.objects.values())
            if len(dispServs) > 0:
                datos = {'dispServs': dispServs}
                datosOrdenados = {'dispServs' : (sorted(datos["dispServs"],key=lambda d: d["id_disp_serv"]))}
            else:
                datos = {'message': "No se encontraron dispServs"}
            return JsonResponse(datosOrdenados)
    def post(self,request):
        jd = json.loads(request.body) 
        print (jd)
        servicio = ServicioExtra.objects.get(id_servicio=jd['id_servicio_id']) 
        zona = Zona.objects.get(id_zona=jd['id_zona_id']) 
        DispServ.objects.create(id_servicio=servicio, id_zona=zona)
        datos = {'message': "Success"}
        return JsonResponse(datos)
