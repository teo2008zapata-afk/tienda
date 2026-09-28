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

def listar(request):
    #Traer todos los registros de la tabla contactos. #Select * from contactos
    productos = producto.objects.all()
    return render(
        request,
        "lista.html",
        {"productos":productos}
    )
