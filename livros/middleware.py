import re
import sys
from django.urls import reverse
from django.shortcuts import redirect

class LoginRequiredMiddleware:
    """Middleware para exigir login em todas as páginas do site, exceto nas páginas de login e registro."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ignorar middleware durante os testes
        if 'test' in sys.argv:
            return self.get_response(request)
        
        allowed_paths = ['/usuarios/login/', '/usuarios/register/']
        
        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect('/usuarios/login/')
        
        return self.get_response(request)
    
class SuperuserRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ignorar middleware durante os testes
        if 'test' in sys.argv:
            return self.get_response(request)

        protected_paths = [
            '/livros/editar', '/deletar_livro', '/categorias/editar',
            '/deletar_categoria', '/autores/editar', '/deletar_autor',
            '/colecoes/editar', '/deletar_colecao',
        ]
        
        for path in protected_paths:
            if re.match(f'^{path}/?', request.path):  
                if not request.user.is_superuser:
                    return redirect(reverse('index'))
        
        return self.get_response(request)