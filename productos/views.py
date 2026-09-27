from django.shortcuts import render
from .models import producto

def crear(request):
    if request.method == 'POST':
        Producto = producto(
            nombre = request.POST["nombre"],
            categoria = request.POST["categoria"],
            precio = request.POST["precio"],
            cantidad = request.POST["cantidad"]
        )
        Producto.save()
    return render(request, "formulario.html")
    return render(request, "prueba.html")
