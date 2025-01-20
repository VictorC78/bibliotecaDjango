from django.shortcuts import redirect

class LoginRequiredMiddleware:
    """Middleware para exigir login em todas as páginas do site, exceto nas páginas de login e registro."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
       
        allowed_paths = ['/usuarios/login/', '/usuarios/register/']
        
        
        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect('/usuarios/login/') 
        return self.get_response(request)
