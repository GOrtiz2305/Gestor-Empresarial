from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import *
from inventario.models import *

# Create your views here.
def nuevo_cliente(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = clienteForm()
        return render(request, 'form_create.html', {'form': form, 'modelo': 'cliente'})
    
def listar_clientes(request):
    queryset = cliente.objects.filter(estado=True)
    clientes_data = [
        {field.name: getattr(item, field.name) for field in cliente._meta.fields}
        for item in queryset
    ]
    return render(request, 'ventas/select_clientes.html', {
        'queryset': clientes_data,
        'modelo': 'cliente'
    })

def editar_cliente(request, id):
    instance = get_object_or_404(cliente, id=id)
    if request.method == 'POST':
        form = clienteForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = clienteForm(instance=instance)
        return render(request, 'form_create.html', {'form': form, 'modelo': 'cliente'})
    
# Borrado logico
def eliminar_cliente(request, id):
    instance = get_object_or_404(cliente, id=id)
    instance.estado = False
    instance.save()
    return redirect('listar_clientes')

def nueva_venta(request):
    if request.method == 'POST':
        form = ventaForm(request.POST)
        form2 = detalle_ventaForm(request.POST)
        if form.is_valid():
            
            # Guardar la venta
            clientee = form.cleaned_data['cliente']
            fecha = form.cleaned_data['fecha']
            total = form.cleaned_data['total']
            venta_final = venta.objects.create(cliente=clientee, fecha=fecha, total=total)

            # Guardar los detalles de la venta (iterar sobre los productos)
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

                    # Guardar cada detalle de venta
                    detalle_venta.objects.create(
                        venta=venta_final,
                        producto=producte,
                        cantidad=cantidad,
                        subtotal=subtotal
                    )

                    producte.stock -= int(cantidad)
                    producte.save()

                    movimiento_inventario.objects.create(
                        tipo='Salida',
                        fecha=fecha,
                        cantidad=cantidad,
                        producto=producte
                    )
            
            return redirect('nueva_venta')
        
        else:
            return HttpResponse('Error en el formulario')
    else:
        form = ventaForm()
        form2 = detalle_ventaForm()
        clientes = cliente.objects.filter(estado=True)
        productos = producto.objects.filter(estado=True)
        return render(request, 'ventas/crear_venta.html', {'form': form, 'form2': form2, 'clientes': clientes, 'productos': productos})
    
def listar_ventas(request):
    # Obtener todas las ventas
    queryset = venta.objects.all()

    ventas_data = []
    
    # Iterar por cada venta y agregar los detalles de venta
    for item in queryset:
        # Obtener todos los detalles de venta relacionados con la venta actual
        detalles_venta = detalle_venta.objects.filter(venta=item)

        # Crear una lista con los detalles de la venta
        detalles_data = [
            {field.name: getattr(detalle, field.name) for field in detalle_venta._meta.fields}
            for detalle in detalles_venta
        ]

        # Agregar la venta con sus detalles al diccionario de ventas
        ventas_data.append({
            field.name: getattr(item, field.name) for field in venta._meta.fields
        })

        # Añadir los detalles al diccionario de cada venta
        ventas_data[-1]['detalles_venta'] = detalles_data

    return render(request, 'ventas/select_ventas.html', {
        'queryset': ventas_data,
        'modelo': 'venta',
    })

def detalles_venta(request, id):
    queryset = detalle_venta.objects.filter(venta=id)
    encabezado = venta.objects.get(id=id)
    detalles_data = [
        {field.name: getattr(item, field.name) for field in detalle_venta._meta.fields}
        for item in queryset
    ]
    return render(request, 'ventas/detalle_venta.html', {
        'queryset': detalles_data, 'modelo': 'detalle_venta' , 'encabezado': encabezado})
