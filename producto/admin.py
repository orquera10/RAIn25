from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre', 'precio', 'stock')
    list_display_links = ('nombre',)
    list_filter = ('categoria',)
    search_fields = ('categoria', 'nombre')
