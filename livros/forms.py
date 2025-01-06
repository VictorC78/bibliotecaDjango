from django import forms
from .models import Categoria

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
