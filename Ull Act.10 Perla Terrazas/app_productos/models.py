from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    # Se agregan default y validaciones para evitar errores de tipo
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    categoria = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_producto})"

    # Método de utilidad para reparar datos inválidos
    @classmethod
    def limpiar_datos_invalidos(cls):
        productos = cls.objects.all()
        for p in productos:
            try:
                # Si precio o stock no son válidos, los corregimos
                if p.precio is None or not isinstance(p.precio, (int, float)):
                    p.precio = 0
                if p.stock is None or not isinstance(p.stock, int):
                    p.stock = 0
                p.save()
            except Exception:
                # Si el valor es string o inválido, forzamos a 0
                try:
                    p.precio = float(p.precio)
                except Exception:
                    p.precio = 0
                try:
                    p.stock = int(p.stock)
                except Exception:
                    p.stock = 0
                p.save()
