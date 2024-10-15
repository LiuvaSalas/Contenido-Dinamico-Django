from django.shortcuts import render

# def mostrandoContenidoDinamico(request):
#    empleados = ["Liuva Salas", "Matias Fuentes", "Isis Gonzalez", "Monica Candia", "Luval Salas", "Diorlette Perez"]
#   context = {"empleados" : empleados}
#    return render(request, "index.html", context)


def plantilla(request):
    return render(request, "index.html ", {})


def herencia1(request):
    return render(request, "herencia1.html", {})
