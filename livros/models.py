from django.db import models

# Create your models here.

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    ano = models.PositiveIntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    colecao = models.ForeignKey('Colecao', on_delete=models.SET_NULL, null=True, blank=True)
    imagem = models.ImageField(upload_to='livros/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

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

    def __str__(self):
        return self.nome
    
class Colecao(models.Model):
    nome = models.CharField(max_length=255, unique= True, verbose_name="Nome da Coleção:")
    descricao = models.TextField(blank= True, null=True, verbose_name="Descrição:")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação:")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização:")

    def __str__(self):
        return self.nome

