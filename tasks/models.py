from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    descricao = models.CharField(max_length=255)
    nome_setor = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    vinculado = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
