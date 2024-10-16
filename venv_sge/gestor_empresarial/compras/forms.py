from django import forms
from .models import *

class proveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = ['nombre', 'direccion', 'telefono', 'contacto_principal']

class compraForm(forms.ModelForm):
    class Meta:
        model = compra
        fields = ['proveedor', 'fecha', 'total']

class detalle_compraForm(forms.ModelForm):
    class Meta:
        model = detalle_compra
        fields = ['compra', 'producto', 'cantidad', 'subtotal']
