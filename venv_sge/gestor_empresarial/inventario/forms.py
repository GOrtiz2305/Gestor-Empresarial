from django import forms
from .models import *

class categoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = ['nombre', 'estado']

class productoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre', 'descripcion', 'precio_venta', 'precio_compra', 'stock', 'categoria', 'proveedor', 'estado']

