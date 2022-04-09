from django.shortcuts import render, get_object_or_404, redirect

from .form import LivrosForm
from .models import Livros

def index(request):
    return render(request, 'livros/base.html')

def listar(request):
    livros = Livros.objects.all()
    return render(request, 'livros/listar.html', {'livros': livros})

def visualizar(request, id):
    livro = get_object_or_404(Livros, pk=id)
    return render(request, 'livros/visualizar.html', {'livro': livro})

#verificar como retornar uma msg na pagina base.html informando que o {{livro.titulo}} foi cadastrado com sucesso.
# messages
def cadastrar(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            livro = form.save()
            return redirect('/listar')
    else:
        form = LivrosForm()
    return render(request, "livros/cadastrar.html", {'form': form} )


#def editar(request, id):


#def deletar(request, id):