from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .form import LivrosForm
from .models import Livros

def index(request):
    return render(request, "livros/base.html")

def listar(request):
    livros = Livros.objects.all()
    return render(request, 'livros/listar.html', {'livros': livros})


def editar(request, id):
    livro = get_object_or_404(Livros, pk=id)
    form = LivrosForm(instance=livro)
    
    if(request.method == 'POST'):
        form = LivrosForm(request.POST, instance=livro)
        
        if(form.is_valid()):
            livro.save()
            return redirect('/')
        else:
            return render(request, 'livros/listar.html', {'form':form, 'livro':livro})
    else:
        return render(request, 'livros/editar.html', {'form':form, 'livro':livro})


def cadastrar(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            livro = form.save()
            return redirect('/')
    else:
        form = LivrosForm()
    return render(request, 'livros/cadastrar.html', {'form': form})


def visualizar(request, id):
    livro = get_object_or_404(Livros, pk = id)
    return render(request, 'livros/visualizar.html', {'livro': livro})

def deletar(request, id):
    livro = get_object_or_404(Livros, pk=id)
    livro.delete()
    messages.info(request, 'Deletado!')
    return redirect('/livros/listar')

#def buscar(request,)