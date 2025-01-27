from django.shortcuts import get_object_or_404, redirect, render
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
        

    return redirect(request.META.get('HTTP_REFERER', '/'))

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

    return redirect(request.META.get('HTTP_REFERER', '/')) 

def reservas(request):
    
    reservados = Reserva.objects.filter(user=request.user)
    favoritos = Favorito.objects.filter(user=request.user).values_list('livro_id', flat=True)
    
    return render(request, 'atividades/reservas.html', {'reservados' : reservados, 'livros_favoritos' : favoritos})

def favoritos(request):
    
    reservado_ids = Reserva.objects.filter(user=request.user).values_list('livro_id', flat=True)
    favoritos = Favorito.objects.filter(user=request.user)
    favoritos_ids = Favorito.objects.filter(user=request.user).values_list('livro_id', flat=True)
    
    return render(request, 'atividades/favoritos.html', {'livros_favoritos' : favoritos, 'favoritos_ids' : favoritos_ids, 'livros_reservados' : reservado_ids})