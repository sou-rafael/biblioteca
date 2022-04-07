from django.shortcuts import render
from .models import Livros

def index(request):
    '''Exibe tanto a pagina incial quanto ja faz uma listagem dos itens'''
    livros = Livros.objects.all()
    return render(request, 'livros/base.html', {'livros': livros})

def editar(request, id):


def deletar(request, id):