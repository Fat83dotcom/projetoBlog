from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post, Categoria
from django.db.models import Q, Count, Case, When


class PostIndex(ListView):
    model = Post
    template_name: str = 'Posts/index.html'
    context_object_name: str = 'posts'
    paginate_by: int = 3

    def get_queryset(self):
        return super().get_queryset().order_by('-id_post').filter(publicado_post=True).annotate(
            numero_comentario=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )


class PostCategoria(PostIndex):
    template_name: str = 'Posts/post_Categoria.html'
    context_object_name: str = 'cat'

    def get_queryset(self):
        return super().get_queryset().all()


class PostBusca(PostIndex):
    template_name: str = 'Posts/post_Busca.html'


class PostDetalhe(UpdateView):
    pass






