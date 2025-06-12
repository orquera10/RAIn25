from django.db import models


class ProductoCategoria(models.Model):
    """Categorías de productos"""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"

class Producto(models.Model):
    categoria = models.ForeignKey(
        ProductoCategoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='categoría',
    )
    nombre = models.CharField(max_length=100, db_index=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name='descripción')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        if self.categoria:
            return f'{self.categoria} - {self.nombre}'
        return self.nombre

    class Meta:
        unique_together = ('categoria', 'nombre')
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'