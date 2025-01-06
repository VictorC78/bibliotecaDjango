from django.shortcuts import redirect, render
from livros.forms import AutorForm, CategoriaForm, ColecaoForm, LivroForm
from livros.models import Autor, Categoria, Colecao, Livro

def index(request):
    categoria_form = CategoriaForm()
    autor_form = AutorForm()
    colecao_form = ColecaoForm()
    livro_form = LivroForm()

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

        elif 'salvar_colecao' in request.POST:
            colecao_form = ColecaoForm(request.POST)
            if colecao_form.is_valid():
                colecao_form.save()
                return redirect('index')

        elif 'salvar_livro' in request.POST:
            livro_form = LivroForm(request.POST, request.FILES)
            if livro_form.is_valid():
                livro_form.save()
                return redirect('index')

    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    colecoes = Colecao.objects.all()
    livros = Livro.objects.all()

    return render(request, 'index.html', {
        'categoria_form': categoria_form,
        'autor_form': autor_form,
        'colecao_form': colecao_form,
        'livro_form': livro_form,
        'categorias': categorias,
        'autores': autores,
        'colecoes': colecoes,
        'livros': livros,
    })
