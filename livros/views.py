from django.shortcuts import get_object_or_404, redirect, render
from livros.forms import AutorForm, CategoriaForm, ColecaoForm, LivroForm
from livros.models import Autor, Categoria, Colecao, Livro

def index(request):

    
    livro_form = LivroForm()

    if request.method == "POST":
        if  'salvar_livro' in request.POST:
            livro_form = LivroForm(request.POST, request.FILES)
            if livro_form.is_valid():
                livro_form.save()
                return redirect('index')

    livros = Livro.objects.all()

    return render(request, 'index.html', {
        
        'livro_form': livro_form,
        'livros': livros,
    })

def categorias(request):
    categoria_form = CategoriaForm()
    
    if request.method == "POST":
        if 'salvar_categoria' in request.POST:
            categoria_form = CategoriaForm(request.POST)
            if categoria_form.is_valid():
                categoria_form.save()
                return redirect('categorias')
            
    categorias = Categoria.objects.all()
    
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
            
    colecoes = Colecao.objects.prefetch_related('livros').all()
    
    return render(request, 'colecoes.html', {
        'colecao_form': colecao_form,
        'colecoes': colecoes,
    })
    
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