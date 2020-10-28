from django.db import models


from cities.models import City
from coverage.models import Coverage
from type_st.models import Type


class Field(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Стадіон')
    coverage = models.ForeignKey(Coverage, on_delete=models.CASCADE, verbose_name='Покриття', related_name='coverage',
                                 default='coverage')
    lighting = models.BooleanField(verbose_name='Освітлення')
    shower = models.BooleanField(verbose_name='Душ')
    section = models.BooleanField(verbose_name="Роздівалки")
    parking = models.BooleanField(verbose_name='Парковка')
    address = models.CharField(max_length=100, verbose_name='Адреса')
    #photo = models.ImageField(verbose_name='Фото')
    size = models.CharField(max_length=100, verbose_name='Розмір')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип поля', related_name='type',
                             default='type')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Місто', related_name='city', default='city')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стадіон'
        verbose_name_plural = 'Стадіони'
        ordering = ['name']



