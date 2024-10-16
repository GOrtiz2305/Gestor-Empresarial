from django.urls import path
from . import views

urlpatterns = [
    path('nuevo_proveedor/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('editar_proveedor/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('pedido/', views.nueva_compra, name='nueva_compra'),
    path('pedidos/', views.listar_compras, name='listar_compras'),
    path('pedido/<int:id>/', views.detalles_compra, name='detalles_compra'),
]