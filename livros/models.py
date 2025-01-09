from django.db import models
from pydantic import ValidationError

# Create your models here.

# Tema do projeto: Biblioteca
# # Dev: Álvaro Victor Carlos Parente - IFSalgueiro

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, related_name="livros")
    ano = models.PositiveIntegerField()
    sinopse = models.TextField(blank=True, null=True, verbose_name="Sinopse:")
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    colecao = models.ForeignKey('Colecao', on_delete=models.SET_NULL, null=True, blank=True, related_name="livros")
    imagem = models.ImageField(upload_to='livros/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def clean(self):
        super().clean()
        if self.ano > 2025:
            raise ValidationError({f'ano': "O ano não pode ser maior que 2025."})

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name="Nome da Categoria:")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição:")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação:")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização:")
    
    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=255, unique= True, verbose_name="Nome do Autor(A):")
    biografia = models.TextField(blank= True, null=True, verbose_name="Biografia do Autor(a):")
    aniversario = models.DateField(verbose_name="Data de Nascimento:")
    nacionalidade = models.CharField(max_length=100, verbose_name="Nacionalidade:")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação:")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização:")
    
    def clean(self):
        super().clean()
        if self.aniversario.year >= 2022:
            raise ValidationError({f'aniversario': "O ano de nasicmento não pode ser maior que 2021."})

    def __str__(self):
        return self.nome
    
class Colecao(models.Model):
    nome = models.CharField(max_length=255, unique= True, verbose_name="Nome da Coleção:")
    descricao = models.TextField(blank= True, null=True, verbose_name="Descrição:")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação:")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização:")

    def __str__(self):
        return self.nome
    
    