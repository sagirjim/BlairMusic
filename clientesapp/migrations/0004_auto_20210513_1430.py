# Generated by Django 3.1.7 on 2021-05-13 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientesapp', '0003_orden_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='client',
            new_name='clientes',
        ),
    ]