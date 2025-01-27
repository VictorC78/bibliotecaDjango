from django.urls import path
from .views import favoritar_livro, favoritos, reservar_livro, reservas

app_name = 'atividades'


urlpatterns = [
    path('favoritar_livro/<int:livro_id>/', favoritar_livro, name='favoritar_livro'),
    path('reservar_livro/<int:livro_id>/', reservar_livro, name='reservar_livro'),
    path('reservas/', reservas, name='reservas'),
    path('favoritos/', favoritos, name='favoritos'),
]
