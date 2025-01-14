from django.shortcuts import get_object_or_404, redirect, render
from livros.forms import AutorForm, CategoriaForm, ColecaoForm, LivroForm
from livros.models import Autor, Categoria, Colecao, Livro

def index(request):

    
    livro_form = LivroForm()
    
    livros = Livro.objects.all()
    colecoes = Colecao.objects.all().order_by("nome")
    autores = Autor.objects.all().order_by("nome")


    colecao_pesquisa = request.GET.get('colecao_pesquisa')  
    autor_pesquisa = request.GET.get('autor_pesquisa')     
    texto_pesquisa = request.GET.get('q', '')                  

    if colecao_pesquisa:
        livros = livros.filter(colecao=colecao_pesquisa)

    if autor_pesquisa:
        livros = livros.filter(autor=autor_pesquisa)

    if texto_pesquisa:
        livros = livros.filter(nome__contains = texto_pesquisa)

    if request.method == "POST":
        if  'salvar_livro' in request.POST:
            livro_form = LivroForm(request.POST, request.FILES)
            if livro_form.is_valid():
                livro_form.save()
                return redirect('index')

    print(livros)
    print(texto_pesquisa)

    return render(request, 'index.html', {
        
        'livro_form': livro_form,
        'livros': livros,
        'colecoes' : colecoes,
        'autores' : autores
    })
    
    
def ver_livro(request, id):
    
    livro = get_object_or_404(Livro, id= id)
    
    livros_relacionados = Livro.objects.filter(
        colecao=livro.colecao,
        categoria=livro.categoria
    ).exclude(id=livro.id)

    return render(request, 'ver_livro.html', {
        'livro': livro,
        'livros_relacionados': livros_relacionados
    })

def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('ver_livro', id= livro.id)
        
    else:
        form = LivroForm(instance=livro)

    return render(request, 'editar_livro.html', {'form': form, 'livro': livro})

def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == "POST":
        if 'confirmar' in request.POST:
            livro.delete()
            return redirect('index') 

    return render(request, 'deletar_livro.html', {'livro': livro})

def categorias(request):
    categoria_form = CategoriaForm()
    
    if request.method == "POST":
        if 'salvar_categoria' in request.POST:
            categoria_form = CategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria_form.save()
                return redirect('categorias')
            
    categorias = Categoria.objects.all().order_by("nome")
    
    return render(request, 'categorias.html', {
        'categoria_form': categoria_form,
        'categorias': categorias,
    })

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias') 
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})

def deletar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == "POST":
        if 'confirmar' in request.POST:
            categoria.delete()
            return redirect('categorias') 

    return render(request, 'deletar_categoria.html', {'categoria': categoria})

def colecoes(request):
    
    colecao_form = ColecaoForm()
    
    if request.method == "POST":
        if 'salvar_colecao' in request.POST:
            colecao_form = ColecaoForm(request.POST)
            if colecao_form.is_valid():
                colecao_form.save()
                return redirect('colecoes')
            
    colecoes = Colecao.objects.prefetch_related('livros').all().order_by("nome")
    
    return render(request, 'colecoes.html', {
        'colecao_form': colecao_form,
        'colecoes': colecoes,
    })
    
def editar_colecao(request, id):
    colecao = get_object_or_404(Colecao, id=id)
    if request.method == 'POST':
        form = ColecaoForm(request.POST, instance=colecao)
        if form.is_valid():
            form.save()
            return redirect('colecoes') 
    else:
        form = ColecaoForm(instance=colecao)

    return render(request, 'editar_colecao.html', {'form': form, 'colecao': colecao})

def deletar_colecao(request, pk):
    colecao = get_object_or_404(Colecao, pk=pk)

    if request.method == "POST":
        if 'confirmar' in request.POST:
            colecao.delete()
            return redirect('colecoes') 

    return render(request, 'deletar_colecao.html', {'colecao': colecao})
    
def autores(request):
    autor_form = AutorForm()
    
    if request.method == "POST":

        if 'salvar_autor' in request.POST:
            autor_form = AutorForm(request.POST)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('autores')
   
    autores = Autor.objects.prefetch_related('livros').all()
    
    return render(request, 'autores.html', {
        'autor_form': autor_form,
        'autores': autores,
    })
    
def editar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autores') 
    else:
        form = AutorForm(instance=autor)

    return render(request, 'editar_autor.html', {'form': form, 'autor': autor})

def deletar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)

    if request.method == "POST":
        if 'confirmar' in request.POST:
            autor.delete()
            return redirect('autores') 

    return render(request, 'deletar_autor.html', {'autor': autor})