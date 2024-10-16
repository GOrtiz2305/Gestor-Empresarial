from django.db import models

# Create your models here.
class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + ' ' + self.direccion + ' ' + self.telefono + ' ' + self.correo
    
class venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.fecha) + ' ' + self.cliente.nombre
    
class detalle_venta(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.ForeignKey(venta, on_delete=models.CASCADE)
    producto = models.ForeignKey('inventario.producto', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cantidad) + ' ' + str(self.subtotal) + ' ' + str(self.venta.fecha) + ' ' + self.producto.nombre