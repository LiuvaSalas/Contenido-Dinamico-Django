from django.shortcuts import render

def mostrandoContenidoDinamico(request):
    empleados = ["Liuva Salas", "Matias Fuentes", "Isis Gonzalez", "Monica Candia", "Luval Salas", "Diorlette Perez"]
    context = {"empleados" : empleados}
    return render(request, "index.html", context)