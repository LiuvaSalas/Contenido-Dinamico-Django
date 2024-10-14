from django.shortcuts import render

def mostrandoContenidoDinamico(request):
    empleados = ["Liuva Salas", "Matias Fuentes", "Isis Gonzalez", "Monica Candia", "Luval Salas", "Diorlette Perez"]
    context = empleados
    return render(request, "contenidoDinamico.html", context)