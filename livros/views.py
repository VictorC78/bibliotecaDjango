from django.shortcuts import redirect, render

from livros.forms import AutorForm, CategoriaForm
from livros.models import Autor, Categoria

def index(request):
    
    categoria_form = CategoriaForm()
    autor_form = AutorForm()

    if request.method == "POST":
        if 'salvar_categoria' in request.POST:
            categoria_form = CategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria_form.save()
                return redirect('index')  

        elif 'salvar_autor' in request.POST:
            autor_form = AutorForm(request.POST)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('index')

    categorias = Categoria.objects.all()
    autores = Autor.objects.all()

    return render(request, 'index.html', {
        'categoria_form': categoria_form,
        'autor_form': autor_form,
        'categorias': categorias,
        'autores': autores,
    })

