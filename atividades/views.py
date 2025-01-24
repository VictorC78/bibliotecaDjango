from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorito, Reserva
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

@login_required
def reservar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    
    reserva_existente = Reserva.objects.filter(livro=livro).first()

    if reserva_existente:
        if reserva_existente.user == request.user:
            
            reserva_existente.delete()
            livro.is_reservado = False  
            livro.save()
        
    else:
        
        Reserva.objects.create(user=request.user, livro=livro)
        livro.is_reservado = True  
        livro.save()

    return redirect('index')  