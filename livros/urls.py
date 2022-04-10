from django.urls import path
from . import views

urlpatterns = [
    path('listar', views.listar, name='listar'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('<int:id>', views.visualizar, name='visualizar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    
]
