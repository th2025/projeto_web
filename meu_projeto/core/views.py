from django.shortcuts import render
from datetime import datetime
from zoneinfo import ZoneInfo
#from django.shortcuts import HttpResponse

# Create your views here.


def homepage(request):
    fusohorario = ZoneInfo("America/Sao_Paulo")
    hora_atual = datetime.now().hour
    hora_completa = datetime.now(fusohorario)
    hora_formatada = hora_completa.strftime("%H:%M:%S")

    if hora_atual < 12:
        saudacao = "Bom dia"
    elif hora_atual < 18:
        saudacao = "Boa tarde"
    else: 
        saudacao = "Boa noite"
    #return HttpResponse("Olá, mundo! Esta é a minha página home")
    contexto = {
        'nome':'Thaylor',
        'saudacao': saudacao,
        'hora' : hora_formatada
        }
    
    return render (request, 'core/index.html', contexto)
