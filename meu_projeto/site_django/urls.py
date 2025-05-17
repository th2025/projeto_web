from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('projeto/', views.projeto, name='projeto'),
    path('projeto/produtos/', views.produto, name='produto'),
    path('registrar/', views.registrar, name='registrar'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
