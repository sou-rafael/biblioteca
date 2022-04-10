from django.forms import ModelForm
from .models import Livros

class LivrosForm(ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'descricao', 'editora', 'quantidade']

# https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
