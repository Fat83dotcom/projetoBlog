from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post-categoria'),
    path('busca/', views.PostBusca.as_view(), name='post-busca'),
    path('post/<int:id>', views.PostDetalhe.as_view(), name='post-detalhes'),
]
