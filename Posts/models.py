from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Categorias.models import Categoria

class Post(models.Model):
    id_post = models.AutoField(primary_key=True, verbose_name='ID')
    titulo_post = models.CharField(max_length=255, null=False, verbose_name='Titulo')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteudo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Categoria')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', null=True, blank=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=False, verbose_name='Pubicado?')

    def __str__(self) -> str:
        return self.titulo_post