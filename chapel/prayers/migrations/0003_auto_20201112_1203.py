# Generated by Django 3.1.2 on 2020-11-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayers', '0002_auto_20201111_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='description',
            field=models.TextField(max_length=220, verbose_name='intenção'),
        ),
    ]
