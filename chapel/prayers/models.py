from django.db import models
from chapel.prayers.managers import LitManager


class Prayer(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('email')
    description = models.TextField('intenção')
    created_at = models.DateTimeField('acesa em', auto_now_add=True)

    objects = LitManager()

    class Meta():
        verbose_name = 'intenção'
        verbose_name_plural = 'intenções'

    def __str__(self):
        return self.name
