from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/cadastro', views.cadastro, name='cadastro'),
    path('/visualizar', views.visualizar, name='home'),
    
]
