from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import RegisterForm

class UsuariosTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testeuser', email='teste@email.com', password='testesenha123')

    
       #Verifica se o formulário de registro é válido quando os dados corretos são fornecidos."""
    def teste_formulario_registro_valido(self):
        form_data = {
            'username': 'novo_usuario',
            'email': 'novo@email.com',
            'password1': 'testesenha123',
            'password2': 'testesenha123',
            'is_superuser': False
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

       #Verifica se o formulário de registro falha ao tentar cadastrar um e-mail já existente."""
    def teste_formulario_registro_email_duplicado(self):
        form_data = {
            'username': 'outro_usuario',
            'email': 'teste@email.com',  
            'password1': 'testesenha123',
            'password2': 'testesenha123',
            'is_superuser': False
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    
       #Verifica se a página de login carrega corretamente."""
    def teste_view_login(self):
        response = self.client.get(reverse('usuarios:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/login.html')

       #Verifica se a página de registro carrega corretamente."""
    def teste_view_registro(self):
        response = self.client.get(reverse('usuarios:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/register.html')

        
       #Verifica se um usuário autenticado pode acessar a página de perfil."""
    def teste_view_perfil_autenticado(self):
        self.client.login(username='testeuser', password='testesenha123')
        response = self.client.get(reverse('usuarios:perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/perfil.html')

       #Verifica se o logout redireciona corretamente."""
    def teste_view_logout(self):
        self.client.login(username='testeuser', password='testesenha123')
        response = self.client.get(reverse('usuarios:logout'))
        self.assertEqual(response.status_code, 302) 

    
       #Verifica se as URLs estão carregando corretamente."""
    def teste_urls_resolvem_corretamente(self):
        self.assertEqual(reverse('usuarios:login'), '/usuarios/login/')
        self.assertEqual(reverse('usuarios:register'), '/usuarios/register/')
        self.assertEqual(reverse('usuarios:logout'), '/usuarios/logout/')
        self.assertEqual(reverse('usuarios:perfil'), '/usuarios/perfil/')
