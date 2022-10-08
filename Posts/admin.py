from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id_post',
        'titulo_post',
        'autor_post',
        'data_post',
        'categoria_post',
        'publicado_post',
    )
    list_editable = ('publicado_post', )
    list_display_links = ('id_post', 'titulo_post', )


admin.site.register(Post, PostAdmin)
