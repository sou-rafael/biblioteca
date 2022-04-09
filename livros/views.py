from django.shortcuts import render, get_object_or_404, redirect


from livros.form import LivrosForm
from .models import Livros

def index(request):
    '''Exibe tanto a pagina incial e ja faz uma listagem dos itens'''
    livros = Livros.objects.all()
    return render(request, 'livros/listar.html', {'livros': livros})

def editar(request, id):
    livro = get_object_or_404(Livros, pk='id')
    form = LivrosForm(instance=livro)
    if(request.method == 'POST'):
        form = LivrosForm(request.POST, instance = novo)
        if(form.is_valid()):
            novo.save()
            return redirect('/')
        else:
            return render(request, '/livros/editar.html', {'form':form, 'livro':livro})
    else:
        return render(request, '/livros/editar.html', {'form':form, 'livro':livro})

def cadastrar(request):
    if request.method == 'POST':
        form = LivrosForm(request.post)
        if form.is_valid():
            livro = form.save()
            return redirect('/')
    else:
        form = LivrosForm()
        return render(request, '/livros/cadastrar.html', {'form': form})

def visualizar(request, id):
    livro = get_object_or_404(Livros, pk = id)
#def deletar(request, id):