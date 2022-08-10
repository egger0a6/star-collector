# Generated by Django 4.1 on 2022-08-10 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_star_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=20)),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.star')),
            ],
        ),
    ]
