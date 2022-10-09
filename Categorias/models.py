from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, verbose_name='ID')
    nome_categoria = models.CharField(max_length=255, unique=True, null=False, verbose_name='Nome')

    def __str__(self) -> str:
        return self.nome_categoria
