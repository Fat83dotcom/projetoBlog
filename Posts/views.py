from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When


class PostIndex(ListView):
    model = Post
    template_name: str = 'Posts/index.html'
    context_object_name: str = 'posts'
    paginate_by: int = 3

    def get_queryset(self):
        return super().get_queryset().order_by('-id_post').annotate(
            numero_comentario=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )


class PostCategoria(PostIndex):
    pass


class PostBusca(PostIndex):
    pass


class PostDetalhe(UpdateView):
    pass






