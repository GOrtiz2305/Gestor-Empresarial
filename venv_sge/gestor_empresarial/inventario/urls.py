from django.urls import path
from . import views

urlpatterns = [
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('editar_categoria/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('eliminar_categoria/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('movimientos/', views.listar_movimientos, name='listar_movimientos'),
]