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
from django.shortcuts import redirect
from django.urls import include, path

from bibliotecaDjango import settings
from django.conf.urls.static import static 
from livros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('atividades/', include('atividades.urls')),
    path('', views.index, name='index'),
    path('letra/<str:letra>/', views.index, name='index_com_letra'),
    path('livro/<int:id>', views.ver_livro, name='ver_livro'),
    path('livros/editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('deletar_livro/<int:pk>/', views.deletar_livro, name='deletar_livro'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('deletar_categoria/<int:pk>/', views.deletar_categoria, name='deletar_categoria'),
    path('colecoes/', views.colecoes, name='colecoes'),
    path('colecoes/editar/<int:id>/', views.editar_colecao, name='editar_colecao'),
    path('deletar_colecao/<int:pk>/', views.deletar_colecao, name='deletar_colecao'),
    path('autores/', views.autores, name='autores'),
    path('autores/editar/<int:id>/', views.editar_autor, name='editar_autor'),
    path('deletar_autor/<int:pk>/', views.deletar_autor, name='deletar_autor'),
    path('sobre/', views.sobre, name='sobre'),
]

if settings.DEBUG:  # Apenas para o modo de desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
