from django.db import models
from apps.categories.models import Category

class Product(models.Model):
    name = models.CharField('Name', max_length=128)
    amout = models.DecimalField(
        'Amount', max_digits=10, decimal_places=2, blank=True, null=True
    )
    category = models.ForeignKey(Category, models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'
