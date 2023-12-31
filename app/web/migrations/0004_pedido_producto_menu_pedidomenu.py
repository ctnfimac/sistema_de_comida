# Generated by Django 4.2.2 on 2023-07-12 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
                ('hora_alta', models.DateTimeField()),
                ('penalizado', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('estado', models.PositiveSmallIntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.cliente')),
                ('comercio', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.comercio')),
                ('repartidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.repartidor')),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='uploads')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('disponible', models.BooleanField(default=True)),
                ('en_stock', models.BooleanField(default=True)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('comercio', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.comercio')),
                ('producto', models.ManyToManyField(related_name='menu_producto', to='web.producto')),
            ],
            options={
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='PedidoMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveSmallIntegerField(default=1)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.menu')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.pedido')),
            ],
            options={
                'verbose_name_plural': 'Menus del Pedido',
                'unique_together': {('pedido', 'menu')},
            },
        ),
    ]
