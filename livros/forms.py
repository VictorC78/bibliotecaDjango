from django import forms
from .models import Autor, Categoria

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
