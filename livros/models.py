from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=300)
    descricao = models.CharField(max_length=400)
    editora = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
