from email.policy import default
from django.db import models
from Posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True, verbose_name='ID')
    titulo_comentario = models.CharField(max_length=255, null=True, verbose_name='Titulo')
    email_comentario = models.EmailField(verbose_name='Email')
    comentario_comentario = models.TextField(verbose_name='Comentario')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuario')
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado?')
