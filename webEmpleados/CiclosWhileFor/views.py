from django.shortcuts import render


def herencia1(request):
    cursos = [
        "Python",
        "Django",
        "Fundamentos del desarrollo web",
        "Bases de datos SQL",
    ]
    return render(request, "WhileFor.html", {"cursos": cursos})
