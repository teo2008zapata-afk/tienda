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
    #Select * from productos
    productos = producto.objects.all()
    return render(
        request,
        "lista.html",
        {"productos":productos}
    )

#Consultar la información de un registro
def detalle(request,id):
    Producto = producto.objects.get(id=id) #SELECT * FROM productos WHERE id=7
    return render(
        request, 
        "detalle.html",
        {"Producto": Producto})

def editar(request, id):
    Producto = producto.objects.get(id=id)#SELECT * FROM productos WHERE id=7
    
    if request.method=="POST":#Si se van a guardar los cambios
        Producto.nombre = request.POST["nombre"] #Cambiar el nombre del producto
        Producto.categoria = request.POST["categoria"] #Cambiar la categoria del producto
        Producto.precio = request.POST["precio"] #Cambiar el precio del producto
        Producto.cantidad = request.POST["cantidad"] #Cambiar la cantidad del producto

        Producto.save() #Guardar los cambios

        return render(
            request,
            "detalle.html",
            {"Producto":Producto}
        )
    return render(
        request,
        "formulario.html",
        {"Producto": Producto}
    )

def eliminar(request,id):
    Producto = producto.objects.get(id=id)#SELECT * FROM producto WHERE id=7
    Producto.delete() #DELETE * FROM producto WHERE id= 7
    return render(
            request,
            "detalle.html",
            {"Producto":Producto}
        )