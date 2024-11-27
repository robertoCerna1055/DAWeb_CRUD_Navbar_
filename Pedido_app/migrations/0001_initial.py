# Generated by Django 5.1.1 on 2024-11-27 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fecha_pedido', models.CharField(max_length=15)),
                ('id_cliente', models.CharField(max_length=6)),
                ('total_pedido', models.CharField(max_length=15)),
                ('fecha_entrega', models.CharField(max_length=20)),
                ('direccion_entrega', models.CharField(max_length=50)),
                ('id_empleado', models.CharField(max_length=6)),
            ],
        ),
    ]