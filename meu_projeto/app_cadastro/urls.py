# app_cadastro/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_cliente, name='cadastro_cliente'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
