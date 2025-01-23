from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorito
from livros.models import Livro

@login_required
def favoritar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    
    favorito = Favorito.objects.filter(user=request.user, livro=livro).first()

    if favorito:
        favorito.delete()  
        
    else:
        Favorito.objects.create(user=request.user, livro=livro)
        

    return redirect('index')
