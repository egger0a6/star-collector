# Generated by Django 4.1 on 2022-08-10 03:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_star_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='age',
            field=models.BigIntegerField(default=1000000000, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50000000000)]),
        ),
    ]
