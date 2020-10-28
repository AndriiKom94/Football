from django.db import models


class Coverage(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Покриття')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Покриття'
        ordering = ['name']

