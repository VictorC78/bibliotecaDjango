from django.shortcuts import redirect, render

from livros.forms import CategoriaForm
from livros.models import Categoria

def index(request):
    categoria_form = CategoriaForm(request.POST)
    
    if request.method == "POST" and 'salvar_categoria' in request.POST:
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            return redirect('index')
    categorias = Categoria.objects.all()  # Recupera todas as categorias para exibição

    return render(request, 'index.html', {
        'categoria_form': categoria_form,
        'categorias': categorias,
    })


