from django.test import TestCase
from django.contrib.auth.models import User
from livros.models import Autor, Categoria, Colecao, Livro
from atividades.models import Favorito, Reserva

class FavoritoReservaTestCase(TestCase):

    def setUp(self):
        # Criar usuários
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

        self.categoria = Categoria.objects.create(nome="Categoria Teste", descricao="Descrição da categoria teste")
        self.autor = Autor.objects.create(
            nome="Autor Teste", 
            biografia="Biografia do autor teste", 
            aniversario="1985-06-15", 
            nacionalidade="Brasileiro"
        )
        self.colecao = Colecao.objects.create(nome="Coleção Teste", descricao="Descrição da coleção teste")
        
        # Criar um livro para os testes de edição e exclusão
        self.livro1 = Livro.objects.create(
            nome='Livro Teste 1',
            autor=self.autor,
            ano=2020,
            sinopse='Sinopse do livro teste 1.',
            categoria=self.categoria,
            colecao=self.colecao
        )
        
        # Criar um livro para os testes de edição e exclusão
        self.livro2 = Livro.objects.create(
            nome='Livro Teste 2',
            autor=self.autor,
            ano=2020,
            sinopse='Sinopse do livro teste 2.',
            categoria=self.categoria,
            colecao=self.colecao
        )
        
        
    def test_favoritar_livro(self):
        # Login do user1
        self.client.login(username='user1', password='password')

        # Verificar que o livro não está favoritado
        self.assertEqual(Favorito.objects.filter(user=self.user1, livro=self.livro1).count(), 0)

        # Favoritar o livro
        response = self.client.get(f'/atividades/favoritar_livro/{self.livro1.id}/')

        # Verificar que o livro foi favoritado
        self.assertEqual(Favorito.objects.filter(user=self.user1, livro=self.livro1).count(), 1)
        self.assertRedirects(response, '/')

        # Desfavoritar o livro
        response = self.client.get(f'/atividades/favoritar_livro/{self.livro1.id}/')

        # Verificar que o livro foi desfavoritado
        self.assertEqual(Favorito.objects.filter(user=self.user1, livro=self.livro1).count(), 0)
        self.assertRedirects(response, '/')

    def test_reservar_livro(self):
        # Login do user1
        self.client.login(username='user1', password='password')

        # Verificar que o livro não está reservado
        self.assertEqual(Reserva.objects.filter(user=self.user1, livro=self.livro1).count(), 0)

        # Reservar o livro
        response = self.client.get(f'/atividades/reservar_livro/{self.livro1.id}/')

        # Verificar que o livro foi reservado
        self.assertEqual(Reserva.objects.filter(user=self.user1, livro=self.livro1).count(), 1)
        self.assertRedirects(response, '/')

        # Cancelar a reserva
        response = self.client.get(f'/atividades/reservar_livro/{self.livro1.id}/')

        # Verificar que a reserva foi removida
        self.assertEqual(Reserva.objects.filter(user=self.user1, livro=self.livro1).count(), 0)
        self.assertRedirects(response, '/')

    

    
