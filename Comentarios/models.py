from email.policy import default
from django.db import models
from Posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    nome_comentario = models.CharField(max_length=255)
    email_comentario = models.EmailField()
    comentario_comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)
