# Generated by Django 4.2.2 on 2023-08-04 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_usuario_contrasenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='key_activacion',
            field=models.CharField(default='', max_length=128),
        ),
    ]
