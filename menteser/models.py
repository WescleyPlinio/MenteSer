from django.db import models

class Transtorno(models.Model):
    nome = models.CharField(max_length=100)
    descricao_tratamento = models.TextField(max_length=500)
    descricao = models.TextField(max_length=500)

    def __str__(self):
        return self.nome
    
class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    icone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class ImagemIndex(models.Model):
    imagem = models.ImageField()
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo