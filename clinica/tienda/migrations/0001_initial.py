# Generated by Django 4.2.7 on 2023-12-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
#Nuestra primer migracion
    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=400, null=True, verbose_name='descripcion')),
            ],
        ),
    ]
