from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.
def ver_evento(request,nome_evento):
    consulta = Evento.objects.get(titulo=nome_evento)
    return HttpResponse('O envento {} está marcado para {}'.format(consulta.titulo, consulta.data_evento))

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request,'agenda.html', dados)

# def index(request):
#     return redirect('/agenda/')