"""
URL configuration for bibliotecaDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bibliotecaDjango import settings
from django.conf.urls.static import static 
from livros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('colecoes/', views.colecoes, name='colecoes'),
    path('autores/', views.autores, name='autores'),
]

if settings.DEBUG:  # Apenas para o modo de desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
