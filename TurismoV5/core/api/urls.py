from django.urls import path
from .views import ZonaView
from .views import DepartamentoView
from .views import ArticuloView
from .views import CategoriaView
from .views import EmpleadoView
from .views import UsuarioView
from .views import TipoUsuarioView
from .views import GastoDeptoView
from .views import EstadoView
from .views import HuespedView
from .views import ReservaView
from .views import DetalleInventarioView
from .views import InventarioView
from .views import MedioPagoView

urlpatterns={
    path('zonas/', ZonaView.as_view(), name='zona'),
    path('zonas/<int:id>', ZonaView.as_view(), name='zona_filtrar'),
    path('departamentos/', DepartamentoView.as_view(), name='departamento'),
    path('departamentos/<int:id>', DepartamentoView.as_view(), name='departmento_filtrar'),
    path('articulos/', ArticuloView.as_view(), name='articulo'),
    path('articulos/<int:id>', ArticuloView.as_view(), name='articulo_filtrar'),
    path('categorias/', CategoriaView.as_view(), name='categoria'),
    path('categorias/<int:id>', CategoriaView.as_view(), name='cateogria_filtrar'),
    path('empleados/', EmpleadoView.as_view(), name='empleado'),
    path('empleados/<int:id>', EmpleadoView.as_view(), name='empleado_filtrar'),
    path('usuarios/', UsuarioView.as_view(), name='usuaio'),
    path('usuarios/<int:id>', UsuarioView.as_view(), name='usuario_filtrar'),
    path('tipoUsuarios/', TipoUsuarioView.as_view(), name='tipoUsuario'),
    path('tipoUsuarios/<int:id>', TipoUsuarioView.as_view(), name='tipoUsuaio_filtrar'),
    path('gastoDeptos/', GastoDeptoView.as_view(), name='gastoDepto'),
    path('gastoDeptos/<int:id>', GastoDeptoView.as_view(), name='gastoDepto_filtrar'),
    path('estadodeptos/', EstadoView.as_view(), name='estado'),
    path('estadoDeptos/<int:id>', EstadoView.as_view(), name='estado_filtrar'),
    path('huespedes/', HuespedView.as_view(), name='huesped'),
    path('huespedes/<int:id>', HuespedView.as_view(), name='huesped_filtrar'),
    path('reservas/', ReservaView.as_view(), name='reserva'),
    path('reservas/<int:id>', ReservaView.as_view(), name='reserva_filtrar'),
    path('detalleInventarios/', DetalleInventarioView.as_view(), name='detalle_inventario'),
    path('detalleInventarios/<int:id>', DetalleInventarioView.as_view(), name='detalle_invantario_filtrar'),
    path('inventarios/', InventarioView.as_view(), name='inventario'),
    path('inventarios/<int:id>', InventarioView.as_view(), name='inventario_filtrar'),
    path('medioPagos/', MedioPagoView.as_view(), name='medioPago'),
    path('medioPagos/<int:id>', MedioPagoView.as_view(), name='medioPago_filtrar')
}