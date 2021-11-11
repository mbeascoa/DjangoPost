
from django.shortcuts import render
from deportes.models import Empleado


def index(request):
     return render(request, "formulariopost/Inicio.html")

def empleados(request):
    ofi = request.POST['txtOficio']
    emple = Empleado()
    cursor=emple.devolverdato(ofi)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "formulariopost/Empleados.html", contexto)
