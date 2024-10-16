from django.db import models
from compras.models import proveedor

# Create your models here.
class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + ' - ' + str(self.stock) + ' - ' + self.categoria.nombre + ' - ' + self.proveedor.nombre
    
class movimiento_inventario(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo + ' - ' + str(self.cantidad) + ' - ' + self.producto.nombre