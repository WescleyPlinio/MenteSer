from django.db import models

class Transtorno(models.Model):
    nome = models.CharField(max_length=100)
    descricao_tratamento = models.TextField(max_length=500)
    descricao = models.TextField(max_length=500)

    def __str__(self):
        return self.nome