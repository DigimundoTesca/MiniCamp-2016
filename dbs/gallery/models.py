from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=48)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return '%s' % self.name


class Card(models.Model):
    name = models.CharField(max_length=48)
    description = models.TextField(null=True, blank=True, default="Describe la tarjeta")
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"

    def __str__(self):
        return '%s' % self.name
