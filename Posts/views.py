from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


class PostIndex(ListView):
    pass


class PostCategoria(PostIndex):
    pass


class PostBusca(PostIndex):
    pass


class PostDetalhe(UpdateView):
    pass






