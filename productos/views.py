from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto


def mostrarIndex(request):
    return render(request, 'index.html')


def mostrarListado(request):
    productos = Producto.objects.all()
    return render(request, 'listado.html', {'productos': productos})


def mostrarFormRegistrar(request):
    return render(request, 'form_registrar.html')


def mostrarFormActualizar(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        producto.nombre = request.POST['txtnom']
        producto.marca = request.POST['cbox']
        producto.precio = request.POST['txtpre']
        producto.save()
        return redirect('productos:listado')

    return render(request, 'form_actualizar.html', {'producto': producto})


def insertarProducto(request):
    if request.method == 'POST':
        nom = request.POST['txtnom']
        mar = request.POST['cbox']
        pre = request.POST['txtpre']

        pro = Producto(nombre=nom, marca=mar, precio=pre)
        pro.save()

        datos = {'msjOk': 'Registro grabado exitosamente'}
        return render(request, 'form_registrar.html', datos)
    else:
        datos = {'msjErr': 'La solicitud no se puede procesar !!'}
        return render(request, 'form_registrar.html', datos)


def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('productos:listado')