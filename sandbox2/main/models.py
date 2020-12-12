from django.db import models

class Category(models.Model):
    name = models.CharField('Categ', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Requests(models.Model):
    title = models.CharField('Название', max_length=100)
    additional_req = models.CharField('Дополнительные требования', max_length=100)
    #categories = models.ManyToManyField(Category)
    how_to_connect = models.CharField('Как связаться', max_length=100)
    description = models.TextField('Описание')
    is_anonimous = models.BooleanField('Анонимно')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'