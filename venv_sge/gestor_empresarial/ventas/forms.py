from django import forms
from .models import *

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'direccion', 'telefono', 'correo', 'estado']

class ventaForm(forms.ModelForm):
    class Meta:
        model = venta
        fields = ['fecha', 'total', 'cliente', 'estado']

class detalle_ventaForm(forms.ModelForm):
    class Meta:
        model = detalle_venta
        fields = ['venta', 'producto', 'cantidad', 'subtotal']
