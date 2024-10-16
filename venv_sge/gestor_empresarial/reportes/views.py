from django.shortcuts import render
from django.db.models import Count
from ventas.models import venta
# Create your views here.

def ventas_por_fecha(request):
    # Agrupar ventas por fecha y contar la cantidad de ventas por día
    ventas_data = venta.objects.values('fecha').annotate(total_ventas=Count('id')).order_by('fecha')

    # Extraer las fechas y los totales para pasarlas al frontend
    fechas = [venta['fecha'] for venta in ventas_data]
    total_ventas = [venta['total_ventas'] for venta in ventas_data]

    return render(request, 'reportes/index.html', {
        'fechas': fechas,
        'total_ventas': total_ventas,
    })