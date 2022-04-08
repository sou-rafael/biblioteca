from django.urls import path
from . import views

urlpatterns = [
    path('livros/atualizar/<int:id>', views.cadastrar, name='cadastrar'),
    path('livros/cadastrar', views.cadastrar, name='cadastrar'),
    path('livros/editar/<int:id>', views.editar, name='editar'),
    path('visualizar/<int:id>', views.visualizar, name='visualizar'),
    #path('/livros/deletar', views.deletar, name='deletar'),
    
]
