from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.

def nueva_categoria(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventario/categorias/')
    else:
        form = categoriaForm()
        return render(request, 'form_create.html', {'form': form, 'modelo': 'categoria'})
    
def listar_categorias(request):
    queryset = categoria.objects.filter(estado=True)
    categorias_data = [
        {field.name: getattr(item, field.name) for field in categoria._meta.fields}
        for item in queryset
    ]
    return render(request, 'inventario/select_categorias.html', {
        'queryset': categorias_data,
        'modelo': 'categoria'
    })

def editar_categoria(request, id):
    instance = get_object_or_404(categoria, id=id)
    if request.method == 'POST':
        form = categoriaForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = categoriaForm(instance=instance)
        return render(request, 'form_create.html', {'form': form, 'modelo': 'categoria'})
    
# Borrado logico
def eliminar_categoria(request, id):
    instance = get_object_or_404(categoria, id=id)
    instance.estado = False
    instance.save()
    return redirect('listar_categorias')

def nuevo_producto(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = productoForm()
        return render(request, 'form_create.html', {'form': form, 'modelo': 'producto'})

def listar_productos(request):
    queryset = producto.objects.filter(estado=True)
    productos_data = [
        {field.name: getattr(item, field.name) for field in producto._meta.fields}
        for item in queryset
    ]
    return render(request, 'inventario/select_productos.html', {
        'queryset': productos_data,
        'modelo': 'producto'
    })

def editar_producto(request, id):
    instance = get_object_or_404(producto, id=id)
    if request.method == 'POST':
        form = productoForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = productoForm(instance=instance)
        return render(request, 'form_create.html', {'form': form, 'modelo': 'producto'})
    
# Borrado logico
def eliminar_producto(request, id):
    instance = get_object_or_404(producto, id=id)
    instance.estado = False
    instance.save()
    return redirect('/inventario/productos/')

def listar_movimientos(request):
    queryset = movimiento_inventario.objects.all()
    movimientos_data = [
        {field.name: getattr(item, field.name) for field in movimiento_inventario._meta.fields}
        for item in queryset
    ]
    return render(request, 'inventario/select_movimientos.html', {
        'queryset': movimientos_data,
        'modelo': 'movimiento'
    })