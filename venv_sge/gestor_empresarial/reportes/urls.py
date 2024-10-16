from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_por_fecha, name='index'),
    #path('grafica/', views.ventas_por_fecha, name='grafica')
]