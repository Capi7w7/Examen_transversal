# Generated by Django 4.1.2 on 2024-07-12 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrito',
            name='repuesto',
        ),
        migrations.DeleteModel(
            name='CarritoCompras',
        ),
        migrations.DeleteModel(
            name='ItemCarrito',
        ),
    ]
