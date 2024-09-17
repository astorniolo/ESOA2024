from django.http import HttpResponse
import datetime
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola mundo")

def verFecha(request):
    fecha_actual=  datetime.datetime.now()
    documento = """ <html>
    <body>
    <h1>HOLA MUNDO</h1>
    <h2>Esta es mi primer pagina</h2>
    <h3> vamos a mostrar datos que el view elabora</h3>
    <p>Fecha y hora actual: %s  este es el marcador de posicion que se reemplaza con el dato</p>
    </body>
    </html>"""%fecha_actual
    return HttpResponse(documento)

def reciboParametro(request,nombre,edad):
    fecha_actual=  datetime.datetime.now()
    documentohtml = """ <html>
    <body>
    <h1>HOLA MUNDO</h1>
    <h1> Soy %s</h1> <h5>edad:%s</h5>
    <h2>Esta es mi primer pagina</h2>
    <h3> vamos a mostrar datos que el view elabora</h3>
    <p>Fecha y hora actual: %s  este es el marcador de posicion que se reemplaza con el dato</p>
    </body>
    </html>"""%(nombre,edad,fecha_actual)
    return HttpResponse(documentohtml)

def conTemplate(request):

    profesor="Andrea"
    alumno="SirBastian"
    materias=["SGBD","AAS","TAP"]

    contexto ={"profesor":profesor,"alumno":alumno,"materias":materias}

    return render(request, "miPagina1.html", contexto)