from django.urls import path
from .views import institucional

urlpatterns = [
    path('institucional/', institucional, name='institucional'),
    #path('institucional/quemsomos/', , name='quemsomos'),
]