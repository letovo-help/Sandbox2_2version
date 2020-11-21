from django.db import models

"""class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name"""

class Requests(models.Model):
    title = models.CharField('Название', max_length=100)
    additional_req = models.CharField('Дополнительные требования', max_length=100)
    categories = models.CharField('Category', max_length=100)
    #categories = models.ManyToManyField('Category', blank=True)
    how_to_connect = models.CharField('Как связаться', max_length=100)
    description = models.TextField('Описание')
    is_anonimous = models.BooleanField('Анонимно')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'