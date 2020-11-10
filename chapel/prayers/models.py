from django.db import models


class Prayer(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('email')
    prayer = models.TextField('preces')
    created_at = models.DateTimeField('acesa em', auto_now_add=True)
