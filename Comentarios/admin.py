from django.contrib import admin
from .models import Comentario

class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'id_comentario',
        'titulo_comentario',
        'email_comentario',
        'comentario_comentario',
        'usuario_comentario',
        'data_comentario',
        'publicado_comentario',
    )
    list_editable = ('publicado_comentario', )
    list_display_links = ('id_comentario', 'titulo_comentario', )


admin.site.register(Comentario, ComentarioAdmin)