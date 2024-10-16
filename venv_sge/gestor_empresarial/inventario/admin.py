from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(categoria)
admin.site.register(producto)
admin.site.register(movimiento_inventario)