from django.shortcuts import render

# Inclui a classe HttpResponse
from django.http import HttpResponse

from blog.models import Post


# Define uma function view chamada index
def index(request):
    # return HttpResponse('Olá Django - index')
    return render(request, "index.html", {"titulo": "Últimos Artigos"})


# Define uma function view chamada ola.
def ola(request):
    # return HttpResponse('Olá Django')
    # return render(request, 'index.html')
    # return render(request, 'home.html')
    posts = Post.objects.all()  # recupera todos os posts do banco de dados
    context = {"posts_list": posts}  # cria um dicionário com os dado
    return render(
        request, "posts.html", context
    )  # renderiza o template e passa o contexto
