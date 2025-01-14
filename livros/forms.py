from django import forms
from .models import Autor, Categoria, Colecao, Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'ano', 'sinopse', 'categoria', 'colecao', 'imagem']  
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
            'autor': forms.Select(attrs={'class': 'form-addlivro'}),
            'ano': forms.NumberInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
            'sinopse': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
            'categoria': forms.Select(attrs={'class': 'form-addlivro'}),
            'colecao': forms.Select(attrs={'class': 'form-addlivro'}),
            'imagem': forms.FileInput(attrs={'class': 'form-addlivro'}),
        }
        labels = {
            'nome': 'Nome do Livro:',
            'autor': 'Autor:',
            'ano': 'Ano:',
            'sinopse' : 'Sinopse',
            'categoria': 'Categoria:',
            'colecao': 'Coleção:',
            'imagem': 'Imagem do Livro:',
        }
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
            'descricao': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
        }
        labels = {
            'nome': 'Nome da Categoria',
            'descricao': 'Descrição',
        }
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'biografia', 'aniversario', 'nacionalidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
            'biografia': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
            'aniversario': forms.DateInput(attrs={'class': 'form-addlivro', 'required': 'required', 'type': 'date'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
        }
        labels = {
            'nome': 'Nome do Autor',
            'biografia': 'Biografia',
            'aniversario': 'Data de Aniversário',
            'nacionalidade': 'Nacionalidade',
        }

class ColecaoForm(forms.ModelForm):
    class Meta:
        model = Colecao
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
            'descricao': forms.TextInput(attrs={'class': 'form-addlivro', 'required': 'required'}),
            
        }
        labels = {
            'nome': 'Nome da coleção:',
            'descricao': 'Descrição da coleção:',
            
        }

