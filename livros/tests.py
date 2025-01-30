from django.test import TestCase
from django.urls import reverse
from livros.models import Autor, Categoria, Colecao, Livro
from livros.forms import AutorForm, CategoriaForm, ColecaoForm, LivroForm

class LivroViewsTest(TestCase):
    def setUp(self):
        
        self.categoria = Categoria.objects.create(nome="Categoria Teste", descricao="Descrição da categoria teste")
        self.autor = Autor.objects.create(
            nome="Autor Teste", 
            biografia="Biografia do autor teste", 
            aniversario="1985-06-15", 
            nacionalidade="Brasileiro"
        )
        self.colecao = Colecao.objects.create(nome="Coleção Teste", descricao="Descrição da coleção teste")
        
        # Criar um livro para os testes de edição e exclusão
        self.livro = Livro.objects.create(
            nome='Livro Teste 1',
            autor=self.autor,
            ano=2020,
            sinopse='Sinopse do livro teste 1.',
            categoria=self.categoria,
            colecao=self.colecao
        )
        
        self.livro_data = {
            'nome': 'Livro Teste 2',
            'autor': self.autor.id,
            'ano': 2020,
            'sinopse': 'Sinopse do livro teste 2.',
            'categoria': self.categoria.id,
            'colecao': self.colecao.id,
            'imagem': None  # Teste sem imagem
        }
        
        # Criar um livro para os testes de edição e exclusão
        self.livro = Livro.objects.create(
            nome='Livro Teste 1',
            autor=self.autor,
            ano=2020,
            sinopse='Sinopse do livro teste 1.',
            categoria=self.categoria,
            colecao=self.colecao
        )
        
    def test_edit_livro(self):
        # Editando o livro
        response = self.client.post(reverse('editar_livro', args=[self.livro.id]), data={
            'nome': 'Livro Editado',
            'autor': self.livro.autor.id,
            'ano': 2021,
            'sinopse': 'Sinopse do livro editado.',
            'categoria': self.livro.categoria.id,
            'colecao': self.livro.colecao.id,
            
        })
        self.assertEqual(response.status_code, 302)  
        self.livro.refresh_from_db() 
        self.assertEqual(self.livro.nome, 'Livro Editado')  

    def test_delete_livro(self):
        response = self.client.post(reverse('deletar_livro', args=[self.livro.id]), data={'confirmar': 'sim'})
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Livro.objects.filter(id=self.livro.id).exists())  

    def test_livro_form_valid(self):
        form = LivroForm(data=self.livro_data)
        self.assertTrue(form.is_valid())  


    def test_livro_form_clean_ano(self):
        # Testar o método clean_ano
        form = LivroForm(data=self.livro_data)
        form.is_valid()  # Validação do formulário
        self.assertEqual(form.cleaned_data['ano'], 2020)


class CategoriaTestCase(TestCase):
    
    
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Ficçãoo", descricao="Livros de romance")

    # Teste para verificar se o formulário é válido com dados corretos
    def test_form_valid(self):
        data = {
            'nome': 'Ficção',
            'descricao': 'Livros de ficção científica'
        }
        form = CategoriaForm(data=data)
        
        
        if not form.is_valid():
            print(form.errors)  
        
        
        self.assertTrue(form.is_valid())

    # Teste para verificar se o formulário é inválido com dados ausentes
    def test_form_invalid(self):
        form_data = {'nome': '', 'descricao': ''}  
        form = CategoriaForm(data=form_data)
        
        
        self.assertFalse(form.is_valid())

    # Teste para verificar se a página de listagem de categorias funciona corretamente
    def test_categorias_view_get(self):
        response = self.client.get(reverse('categorias'))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'livros/listar/categorias.html')  
        self.assertContains(response, 'Ficçãoo')  

    # Teste para verificar se a página de edição de uma categoria específica funciona
    def test_editar_categoria_view_get(self):
        response = self.client.get(reverse('editar_categoria', args=[self.categoria.id]))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'livros/editar/editar_categoria.html')  
        self.assertContains(response, 'Ficçãoo')  

    # Teste para verificar se a página de exclusão de uma categoria específica funciona
    def test_deletar_categoria_view_get(self):
        response = self.client.get(reverse('deletar_categoria', args=[self.categoria.id]))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'livros/deletar/deletar_categoria.html')  
        self.assertContains(response, 'Ficçãoo')  

    # Teste para verificar se a exclusão da categoria é bem-sucedida com a confirmação do formulário
    def test_deletar_categoria_view_post(self):
        response = self.client.post(reverse('deletar_categoria', args=[self.categoria.id]), {'confirmar': 'true'})  
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Categoria.objects.filter(id=self.categoria.id).exists()) 
        
        # Verifica se a URL de categorias resolve para a view correta
    def test_categorias_url(self):
        response = self.client.get('/categorias/')
        self.assertEqual(response.status_code, 200)

        # Verifica se a URL de edição de categoria resolve para a view correta
    def test_editar_categoria_url(self):
        response = self.client.get(f'/categorias/editar/{self.categoria.id}/')
        self.assertEqual(response.status_code, 200)

        # Verifica se a URL de deletar categoria resolve para a view correta
    def test_deletar_categoria_url(self):
        response = self.client.get(f'/deletar_categoria/{self.categoria.id}/')
        self.assertEqual(response.status_code, 200)

class ColecaoTestCase(TestCase):
    
    def setUp(self):
        
        self.colecao = Colecao.objects.create(nome="Coleção de Ficção", descricao="Coleção de livros de ficção")

    def test_form_valid(self):
        
        data = {
            'nome': 'Coleção Aventura',
            'descricao': 'Livros de aventuras incríveis'
        }
        form = ColecaoForm(data=data)
        
        
        if not form.is_valid():
            print(form.errors)  
        
        
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        # Teste para verificar se o formulário é inválido com dados ausentes
        form_data = {'nome': '', 'descricao': ''}  
        form = ColecaoForm(data=form_data)
        
        # Verifica se o formulário foi corretamente identificado como inválido
        self.assertFalse(form.is_valid())

    def test_colecoes_view_get(self):
        # Teste para verificar a URL de listagem de coleções
        response = self.client.get(reverse('colecoes'))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'livros/listar/colecoes.html')  
        self.assertContains(response, 'Coleção de Ficção')  

    def test_editar_colecao_view_get(self):
        # Teste para verificar a URL de edição de uma coleção
        response = self.client.get(reverse('editar_colecao', args=[self.colecao.id]))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'livros/editar/editar_colecao.html')  
        self.assertContains(response, 'Coleção de Ficção')  

    def test_deletar_colecao_view_get(self):
        # Teste para verificar a URL de exclusão de uma coleção
        response = self.client.get(reverse('deletar_colecao', args=[self.colecao.id]))  
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'livros/deletar/deletar_colecao.html')  
        self.assertContains(response, 'Coleção de Ficção')  

    def test_deletar_colecao_view_post(self):
        # Teste para verificar a exclusão da coleção com a confirmação do formulário
        response = self.client.post(reverse('deletar_colecao', args=[self.colecao.id]), {'confirmar': 'true'})  
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Colecao.objects.filter(id=self.colecao.id).exists())  

    # Testes das URLs diretamente

    def test_colecoes_url(self):
        # Verifica se a URL de coleções resolve para a view correta
        response = self.client.get('/colecoes/')
        self.assertEqual(response.status_code, 200)

    def test_editar_colecao_url(self):
        # Verifica se a URL de edição de coleção resolve para a view correta
        response = self.client.get(f'/colecoes/editar/{self.colecao.id}/')
        self.assertEqual(response.status_code, 200)

    def test_deletar_colecao_url(self):
        # Verifica se a URL de deletar coleção resolve para a view correta
        response = self.client.get(f'/deletar_colecao/{self.colecao.id}/')
        self.assertEqual(response.status_code, 200)
        
class AutorTestCase(TestCase):
    
    def setUp(self):
        # Criação de um autor para ser usado nos testes
        self.autor = Autor.objects.create(
            nome="Autor Teste",
            biografia="Biografia do autor teste",
            aniversario="1980-01-01",
            nacionalidade="Brasileiro"
        )

    def test_form_valid(self):
        # Teste para validar o formulário com dados corretos
        data = {
            'nome': 'Autor Valido',
            'biografia': 'Biografia do autor valido',
            'aniversario': '1990-05-15',
            'nacionalidade': 'Brasileiro'
        }
        form = AutorForm(data=data)
        
        # Se o formulário não for válido, imprime os erros para ajudar na depuração
        if not form.is_valid():
            print(form.errors)  
        
        # Verifica se o formulário foi validado corretamente
        self.assertTrue(form.is_valid())


    def test_autores_view_get(self):
        # Teste para verificar a URL de listagem de autores
        response = self.client.get(reverse('autores'))  # Realiza a requisição GET
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta tem status 200 (OK)
        self.assertTemplateUsed(response, 'livros/listar/autores.html')  # Verifica se a template correta é usada
        self.assertContains(response, 'Autor Teste')  # Verifica se o nome do autor criado aparece na página

    def test_editar_autor_view_get(self):
        # Teste para verificar a URL de edição de um autor
        response = self.client.get(reverse('editar_autor', args=[self.autor.id]))  # Requisição GET para editar
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta tem status 200 (OK)
        self.assertTemplateUsed(response, 'livros/editar/editar_autor.html')  # Verifica a template usada
        self.assertContains(response, 'Autor Teste')  # Verifica se o nome do autor aparece na página de edição

    def test_deletar_autor_view_get(self):
        # Teste para verificar a URL de exclusão de um autor
        response = self.client.get(reverse('deletar_autor', args=[self.autor.id]))  # Requisição GET para deletar
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta tem status 200 (OK)
        self.assertTemplateUsed(response, 'livros/deletar/deletar_autor.html')  # Verifica a template usada
        self.assertContains(response, 'Autor Teste')  # Verifica se o nome do autor aparece na página de exclusão

    def test_deletar_autor_view_post(self):
        # Teste para verificar a exclusão do autor com a confirmação do formulário
        response = self.client.post(reverse('deletar_autor', args=[self.autor.id]), {'confirmar': 'true'})  # Requisição POST confirmando a exclusão
        self.assertEqual(response.status_code, 302)  # Verifica se houve redirecionamento após exclusão
        self.assertFalse(Autor.objects.filter(id=self.autor.id).exists())  # Verifica se o autor foi realmente deletado

    # Testes das URLs diretamente

    def test_autores_url(self):
        # Verifica se a URL de autores resolve para a view correta
        response = self.client.get('/autores/')
        self.assertEqual(response.status_code, 200)

    def test_editar_autor_url(self):
        # Verifica se a URL de editar autor resolve para a view correta
        response = self.client.get(f'/autores/editar/{self.autor.id}/')
        self.assertEqual(response.status_code, 200)

    def test_deletar_autor_url(self):
        # Verifica se a URL de deletar autor resolve para a view correta
        response = self.client.get(f'/deletar_autor/{self.autor.id}/')
        self.assertEqual(response.status_code, 200)