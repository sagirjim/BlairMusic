from django.shortcuts import render, redirect, get_object_or_404
from .forms import clienteForm, ordenForm
from .models import Cliente, Orden
from .filters import ClienteFilter
from django.contrib import messages




def home(request):
    return render(request, 'home.html', {})


def clientesindex(request):

    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        cliente = Cliente.objects.all()
        for item in cliente:
            indice = item.id
            if nombre == item.nombre:
                return redirect("clientepag", id=indice)
            else:
                messages.error(request, "No se encontro cliente con ese Nombre")

    if 'cedula' in request.GET:
        cedula = request.GET['cedula']
        cliente = Cliente.objects.all()
        for item in cliente:
            indice = item.id
            if cedula == item.cedula:
                return redirect("clientepag", id=indice)
            else:
                messages.error(request, "No se encontro cliente con ese numero de Cedula")


    return render(request, "clientesindex.html", {})

def orderforclient(request):

    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        cliente = Cliente.objects.all()
        for item in cliente:
            indice = item.id
            if nombre == item.nombre:
                return redirect("clientepag", id=indice)
            else:
                messages.error(request, "No se encontro cliente con ese Nombre")
    if 'cedula' in request.GET:
        cedula = request.GET['cedula']
        cliente = Cliente.objects.all()
        for item in cliente:
            indice = item.id
            if cedula == item.cedula:
                return redirect("clientepag", id=indice)
            else:
                messages.error(request, "No se encontro cliente con ese numero de Cedula")


    return render(request, "orderforclient.html", {})


def clnt(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            init = form.save()

            return redirect("clientepag", id=init.id)

    else:
        form = clienteForm()
    return render(request, 'index.html', {'form': form})


def view(request):
    cliente = Cliente.objects.all()
    return render(request, "view.html", {'cliente': cliente})


def delete(request, id):
    otro = Cliente.objects.filter(id=id)
    otro.delete()
    return redirect('/view')


def edit(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "edit.html", {'cliente': cliente})


def update(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'GET':
        form = clienteForm(instance=cliente)
        return redirect("clientepag", id=id)

    else:
        form = clienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect("clientepag", id=id)
        else:
            form = clienteForm()
            return redirect("clientepag", id=id)


def clientepag(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'clientepag.html', {'cliente': cliente})


def ordenindex(request):

    if 'orden' in request.GET:
        orden = request.GET['orden']
        ordenes = Orden.objects.all()
        for item in ordenes:
            indice = item.id
            if orden == item.num_orden:
                return redirect("ordenview", id=indice)
            else:
                messages.error(request, "No se encontro una Orden con ese numero")


    return render(request, "ordenindex.html", {})


def ordenfill(request):

    if request.method == 'POST':
        orden = ordenForm(request.POST)
        print(orden.errors)
        if orden.is_valid():
            init = orden.save()
            return redirect('ordenview', id=init.id)

    else:
        orden = ordenForm()
    return render(request, 'ordenfill.html', {'orden': orden})


def ordenview(request, id):
    orden = Orden.objects.get(id=id)
    return render(request, 'ordenview.html', {'orden': orden})


def ordenupd(request, id):
    orden = Orden.objects.get(id=id)
    return render(request, "ordenupd.html", {'orden': orden})


def ordenmod(request, id):
    orden = get_object_or_404(Orden, id=id)

    if request.method == 'GET':
        orden = ordenForm(instance=orden)
        return redirect("ordenview", id=id)

    else:

        orden = ordenForm(request.POST, instance=orden)

        if orden.is_valid():
            orden.save()
            return redirect("ordenview", id=id)
        else:
            orden = clienteForm()
            return redirect("ordenview", id=id)
