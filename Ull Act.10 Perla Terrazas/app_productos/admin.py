from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'descripcion', 'precio', 'stock', 'categoria')
    search_fields = ('nombre', 'categoria')
