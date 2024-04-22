# Generated by Django 5.0.1 on 2024-01-11 17:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='actualizacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de Edición'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='autor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categoria',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de Creación'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Descripción'),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True, verbose_name='Nombre')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/%Y/$m/%d', verbose_name='Imagen')),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Productos', to=settings.AUTH_USER_MODEL)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria', verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('productos', models.ManyToManyField(to='tienda.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.pedido')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
    ]