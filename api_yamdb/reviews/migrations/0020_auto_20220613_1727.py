# Generated by Django 2.2.16 on 2022-06-13 14:27

import django.core.validators
import reviews.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0019_auto_20220613_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(reviews.utils.get_year)], verbose_name='Год выхода'),
        ),
    ]
