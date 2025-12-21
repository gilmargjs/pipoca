from django.contrib import admin
from pipoca.models import Pipoca,Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

# Register your models here.
class PipocaAdmin(admin.ModelAdmin):
    list_display = ('sabor', 'categoria', 'preco','imagem')
    search_fields = ('sabor',)

admin.site.register(Pipoca, PipocaAdmin)
admin.site.register(Categoria, CategoriaAdmin)