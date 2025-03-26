from django.db import models

class Category(models.Model):
    name = models.CharField('Name', max_length=128)

    def __str__(self):
        return f'{self.name}'
