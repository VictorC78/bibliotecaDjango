from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name="Nome da Categoria:")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    
    def __str__(self):
        return self.nome
