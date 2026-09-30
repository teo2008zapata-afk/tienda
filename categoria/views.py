from django.shortcuts import render
from .models import categoria

def crear(request):
    if request.method == 'POST':
        Categoria = categoria(
            nombre = request.POST["nombre"],
            observaciones = request.POST["observaciones"]
        )
        Categoria.save()
    return render(request, "formulario_categoria.html")

def listar(request):
    #Select * from categorias
    categorias = categoria.objects.all()
    return render(
        request,
        "lista_categoria.html",
        {"categorias":categorias}
    )

#Consultar la información de un registro
def detalle(request,id):
    Categoria = categoria.objects.get(id=id) #SELECT * FROM categorias WHERE id=7
    return render(
        request, 
        "detalle_categoria.html",
        {"Categoria": Categoria})

def editar(request, id):
    Categoria = categoria.objects.get(id=id)#SELECT * FROM categorias WHERE id=7
    
    if request.method=="POST":#Si se van a guardar los cambios
        Categoria.nombre = request.POST["nombre"] #Cambiar el nombre de la categoria
        Categoria.observaciones = request.POST["observaciones"] #Cambiar las observaciones de la categoria

        Categoria.save() #Guardar los cambios

        return render(
            request,
            "detalle_categoria.html",
            {"Categoria":Categoria}
        )
    return render(
        request,
        "formulario_categoria.html",
        {"Categoria": Categoria}
    )

def eliminar(request,id):
    Categoria = categoria.objects.get(id=id)#SELECT * FROM categoria WHERE id=7
    Categoria.delete() #DELETE * FROM categoria WHERE id= 7
    return render(
            request,
            "lista_categoria.html",
            {"Categoria":Categoria}
        )
