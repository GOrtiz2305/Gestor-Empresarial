from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import *
from inventario.models import *

# Create your views here.

def nuevo_proveedor(request):
    if request.method == 'POST':
        form = proveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = proveedorForm()
        return render(request, 'form_create.html', {'form': form, 'modelo': 'proveedor'})
    
def listar_proveedores(request):
    queryset = proveedor.objects.filter(estado=True)
    proveedores_data = [
        {field.name: getattr(item, field.name) for field in proveedor._meta.fields}
        for item in queryset
    ]
    return render(request, 'compras/select_proveedores.html', {
        'queryset': proveedores_data,
        'modelo': 'proveedor'
    })

def editar_proveedor(request, id):
    instance = get_object_or_404(proveedor, id=id)
    if request.method == 'POST':
        form = proveedorForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = proveedorForm(instance=instance)
        return render(request, 'form_create.html', {'form': form, 'modelo': 'proveedor'})
    
# Borrado logico
def eliminar_proveedor(request, id):
    instance = get_object_or_404(proveedor, id=id)
    instance.estado = False
    instance.save()
    return redirect('listar_proveedores')

def nueva_compra(request):
    if request.method == 'POST':
        form = compraForm(request.POST)
        form2 = detalle_compraForm(request.POST)
        if form.is_valid():
            
            # Guardar la compra
            proveedore = form.cleaned_data['proveedor']
            fecha = form.cleaned_data['fecha']
            total = form.cleaned_data['total']
            compra_final = compra.objects.create(proveedor=proveedore, fecha=fecha, total=total)

            # Guardar los detalles de la compra (iterar sobre los productos)
            productos = request.POST.getlist('producto[]')
            cantidades = request.POST.getlist('cantidad[]')
            precios = request.POST.getlist('precio[]')
            subtotales = request.POST.getlist('subtotal[]')

            for i in range(len(productos)):
                if productos[i]:  # Verificar que el producto no esté vacío
                    producte = producto.objects.get(id=productos[i])  # Obtener el objeto de producto
                    cantidad = cantidades[i]
                    precio = precios[i]
                    subtotal = subtotales[i]

                    # Guardar cada detalle de compra
                    detalle_compra.objects.create(
                        compra=compra_final,
                        producto=producte,
                        cantidad=cantidad,
                        subtotal=subtotal
                    )

                    producte.stock += int(cantidad)
                    producte.save()

                    movimiento_inventario.objects.create(
                        tipo='Entrada',
                        fecha=fecha,
                        cantidad=cantidad,
                        producto=producte
                    )
            
            return redirect('nueva_compra')
        
        else:
            return HttpResponse('Error en el formulario')
    else:
        form = compraForm()
        form2 = detalle_compraForm()
        proveedores = proveedor.objects.filter(estado=True)
        productos = producto.objects.filter(estado=True)
        return render(request, 'compras/crear_compra.html', {'form': form, 'form2': form2, 'proveedores': proveedores, 'productos': productos})
    
def listar_compras(request):
    queryset = compra.objects.all()
    compras_data = [
        {field.name: getattr(item, field.name) for field in compra._meta.fields}
        for item in queryset
    ]
    return render(request, 'compras/select_compras.html', {
        'queryset': compras_data,
        'modelo': 'compra'
    })

def detalles_compra(request, id):
    queryset = detalle_compra.objects.filter(compra=id)
    encabezado = compra.objects.get(id=id)
    detalles_data = [
        {field.name: getattr(item, field.name) for field in detalle_compra._meta.fields}
        for item in queryset
    ]
    return render(request, 'compras/detalle_compra.html', {
        'queryset': detalles_data, 'modelo': 'detalle_compra' , 'encabezado': encabezado})
