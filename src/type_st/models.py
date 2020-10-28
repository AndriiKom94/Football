from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тип поля')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип поля'
        ordering = ['name']
