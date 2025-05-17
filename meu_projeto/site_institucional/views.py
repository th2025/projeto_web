from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def institucional(request):
    return render(request, 'site_institucional/index.html')

#def quemsomos(request):
    return HttpResponse("Quem somos")


