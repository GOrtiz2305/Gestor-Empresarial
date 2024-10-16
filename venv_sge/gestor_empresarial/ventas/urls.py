from django.urls import path
from . import views

urlpatterns = [
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('venta/', views.nueva_venta, name='nueva_venta'),
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('venta/<int:id>/', views.detalles_venta, name='detalles_venta'),
]