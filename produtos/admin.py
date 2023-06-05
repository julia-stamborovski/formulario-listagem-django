from django.contrib import admin

from .models import Produto

class ListagemProdutos(admin.ModelAdmin):
    list_display = ("nome", "descricao", "preco", "disponivel")
    list_display_links = ("nome", "descricao")
    search_fields = ("nome",)
    list_filter = ("disponivel",)
admin.site.register(Produto, ListagemProdutos)
