from django.db import models


class Contacts(models.Model):
    name = models.CharField('Имя', max_length=50)
    preview = models.CharField('Краткая информация', max_length=200)
    country = models.CharField('Страна', max_length=50)
    town = models.CharField('Город', max_length=50)
    organization = models.CharField('Организация', max_length=50)
    telephone = models.PositiveBigIntegerField('Телефон')
    email = models.EmailField('Электронная почта', max_length=50)
    date_of_creation = models.DateField('Дата создания', auto_now_add=True)
    date_of_change = models.DateField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
