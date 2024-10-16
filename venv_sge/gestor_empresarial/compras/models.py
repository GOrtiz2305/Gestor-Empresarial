from django.db import models

# Create your models here.
class proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    contacto_principal = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + ' - ' + self.direccion + ' - ' + self.telefono + ' - ' + self.contacto_principal
    
class compra(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.proveedor.nombre + ' - ' + str(self.fecha) + ' - ' + str(self.total)
    
class detalle_compra(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    compra = models.ForeignKey(compra, on_delete=models.CASCADE)
    producto = models.ForeignKey('inventario.producto', on_delete=models.CASCADE)

    def __str__(self):
        return self.producto.nombre + ' - ' + str(self.cantidad) + ' - ' + str(self.subtotal)