from django.shortcuts import render

def index(request):
    return render(request, 'livros/base.html')